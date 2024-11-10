#!/usr/bin/env python3
""" task0: Writing strings to Redis """

import redis
import uuid
from typing import Union


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