#!/usr/bin/env python3
""" task0: Writing strings to Redis """

import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """ cache redis class """
    def __init__(self):
        """ constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores data in Redis and returns the generated key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) ->\
            Union[bytes, str, int, float, None]:
        """ convert data to desired format using Callable """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Retrieve the value and decode it to a string """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve the value and decode it to an integer """
        return self.get(key, fn=lambda d: int(d))
