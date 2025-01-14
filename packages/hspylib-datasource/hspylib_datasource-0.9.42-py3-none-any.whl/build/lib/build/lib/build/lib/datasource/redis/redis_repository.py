#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HsPyLib-Datasource
   @package: datasource.postgres
      @file: postgres_repository.py
   @created: Sat, 12 Nov 2022
    @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior"
      @site: https://github.com/yorevs/hspylib
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""
from abc import abstractmethod
from datasource.crud_entity import CrudEntity
from datasource.db_repository import Connection, Cursor
from datasource.exception.exceptions import DatabaseConnectionError, DatabaseError
from datasource.redis.redis_configuration import RedisConfiguration
from hspylib.core.enums.charset import Charset
from hspylib.core.metaclass.singleton import AbstractSingleton
from hspylib.core.preconditions import check_not_none
from redis.client import Pipeline
from retry import retry
from typing import Generic, List, Optional, Tuple, TypeVar

import contextlib
import logging as log
import redis

E = TypeVar("E", bound=CrudEntity)


class RedisRepository(Generic[E], metaclass=AbstractSingleton):
    """Implementation of a data access layer for a postgres persistence store.
    Ref.: https://github.com/redis/redis-py
    Ref.: https://docs.redis.com/latest/rs/references/client_references/client_python/
    """

    def __init__(self, config: RedisConfiguration):
        self._config = config

    def __str__(self):
        return f"{self.hostname}:{self.port}/{self.database}"

    def __repr__(self):
        return str(self)

    @property
    def logname(self) -> str:
        return self.__class__.__name__.split("_", maxsplit=1)[0]

    @property
    def hostname(self) -> str:
        return self._config.hostname

    @property
    def port(self) -> int:
        return self._config.port

    @property
    def database(self) -> str:
        return self._config.database

    @property
    def password(self) -> str:
        return self._config.password

    @property
    def ssl(self) -> bool:
        return self._config.ssl

    @retry(tries=3, delay=2, backoff=3, max_delay=30)
    def _create_session(self) -> Tuple[Connection, Cursor]:
        """Connect and create a database session."""
        log.debug("%s Attempt to connect to database: %s", self.logname, str(self))
        conn = redis.Redis(ssl=self.ssl, host=self.hostname, port=self.port, password=self.password)
        log.debug("%s Connection info: %s", self.logname, conn.config_get("databases"))
        return conn, conn.pipeline()

    @contextlib.contextmanager
    def pipeline(self) -> Pipeline:
        """Generator to create a database pipeline and return it."""
        pipe = None
        try:
            _, pipe = self._create_session()
            log.debug("%s Successfully connected to database: %s [ssid=%d]", self.logname, str(self), hash(pipe))
            yield pipe
        except redis.exceptions.ConnectionError as err:
            raise DatabaseConnectionError(f"Unable to open/execute-on database session => {err}") from err
        except redis.exceptions.ResponseError as err:
            log.error("%s Pipeline failed with: %s", self.logname, err)
        except Exception as err:
            raise DatabaseError(f"{self.logname} Unable to execute pipeline -> {err}") from err
        finally:
            if pipe:
                pipe.close()

    def mget(self, *keys: str) -> List[E]:
        """Returns the values of all specified keys. For every key that does not hold a string value or does not exist,
        the special value nil is returned. Because of this, the operation never fails.
        :param keys: the list of keys to get.
        """
        check_not_none(keys)
        with self.pipeline() as pipe:
            result = []
            pipe.mget(keys)
            count = len(pipe)
            ret_val = list(filter(None, pipe.execute()))
            if ret_val:
                list(map(lambda e: result.append(self.to_entity_type(e)), ret_val[0]))
            log.debug(
                "%s Executed '%s' pipelined 'GET' command(s) and returned %d entries", self.logname, count, len(result)
            )
            return result

    def get(self, key: str) -> Optional[E]:
        """Get the value of key. If the key does not exist the special value nil is returned. An error is returned if
        the value stored at key is not a string, because GET only handles string values.
        :param key: the key to get.
        """
        check_not_none(key)
        with self.pipeline() as pipe:
            pipe.get(key)
            ret_val = list(filter(None, pipe.execute()))
            log.debug("%s Executed a pipelined 'GET' command and returned: %s", self.logname, ret_val)
            return self.to_entity_type(ret_val[0]) if ret_val else None

    def set(self, *entities: E) -> Optional[List[E]]:
        """Set key to hold the string value. If key already holds a value, it is overwritten, regardless of its type.
        Any previous time to live associated with the key is discarded on successful SET operation.
        :param entities the entities to set.
        """
        check_not_none(entities)
        with self.pipeline() as pipe:
            list(map(lambda e: pipe.set(self.build_key(e), str(e._asdict())), entities))
            count = len(pipe)
            log.debug("%s Executing '%d' pipelined 'SET' command(s)", self.logname, count)
            return pipe.execute()

    def delete(self, *keys: str) -> int:
        """Removes the specified keys. A key is ignored if it does not exist.
        :param keys: the keys to delete.
        """
        check_not_none(keys)
        with self.pipeline() as pipe:
            pipe.delete(*keys)
            ret_val = pipe.execute() or []
            log.debug("%s Executed a pipelined 'DEL' command and returned: %s", self.logname, ret_val)
            return ret_val[0] or 0

    def flushdb(self) -> None:
        """Delete all the keys of the currently selected DB. This command never fails."""
        with self.pipeline() as pipe:
            pipe.flushall()
            pipe.execute()
            log.debug("%s Executed a FLUSHDB command", self.logname)

    def keys(self, pattern: str) -> List[str]:
        """Returns all keys matching pattern.
        :param pattern: the glob-style pattern to match against.
        """
        with self.pipeline() as pipe:
            pipe.keys(pattern)
            ret_val = list(filter(None, pipe.execute()))
            result = list(map(lambda k: str(k, Charset.UTF_8.val), ret_val[0])) if ret_val else []
            log.debug("%s Executed a KEYS command and returned: %d entries", self.logname, len(ret_val))
            return result

    @abstractmethod
    def build_key(self, entity: E) -> str:
        """Builds an appropriate key for the entity.
        :param entity: the entity to build a key for.
        """

    @abstractmethod
    def to_entity_type(self, entity_string: str | bytes) -> E:
        """Convert a string into the CRUD entity.
        :param entity_string: the entity string or bytes to be converted.
        """
