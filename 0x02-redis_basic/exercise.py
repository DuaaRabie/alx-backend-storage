#!/usr/bin/env python3
""" task0: Writing strings to Redis """

import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called"""
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        # Use the qualified name of the method as the Redis key
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        method_key = method.__qualname__
        self._redis.rpush(f"{method_key}:inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{method_key}:outputs", result)
        return result
    return wrapper


def replay(method: Callable) -> Callable:
    """ display the history of calls of a particular function """
    method_key = method.__qualname__
    inputs = method.__self__._redis.lrange(f"{method_key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{method_key}:outputs", 0, -1)
    print(f"{method_key} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        input_args = eval(input_args.decode("utf-8"))
        print(f"{method_key}(*{input_args}) -> {output.decode('utf-8')}")


class Cache:
    """ cache redis class """
    def __init__(self):
        """ constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
