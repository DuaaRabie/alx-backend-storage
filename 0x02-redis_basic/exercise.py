#!/usr/bin/env python3
""" task0: Writing strings to Redis """

import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        # Use the qualified name of the method as the Redis key
        method_key = method.__qualname__
        if self._redis.get(method_key) is None:
            self._redis.set(method_key, 0)
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ cache redis class """
    def __init__(self):
        """ constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores data in Redis and returns the generated key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[bytes, str, int, float, None]:
        """ convert data to desired format using Callable """
        data = self._redis.get(key)
        if data is None:
            return None
        try:
            if fn:
                return fn(data)
            return data
        except ValueError:
            raise ValueError

    def get_str(self, key: str) -> str:
        """ Retrieve the value and decode it to a string """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve the value and decode it to an integer """
        return self.get(key, fn=lambda d: int(d))
