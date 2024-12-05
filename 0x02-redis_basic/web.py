#!/usr/bin/env python3
"""  Implementing an expiring web cache and tracker
"""
import redis
import requests
import time
from functools import wraps


# Create a Redis client
redis_client = redis.Redis()


def count_and_cache(fn):
    """Decorator to count access and cache the result"""
    @wraps(fn)
    def wrapper(url: str):
        # Increment the count for this URL
        redis_client.incr(f"count:{url}")

        # Check if the page is cached
        cached_page = redis_client.get(url)
        if cached_page:
            return cached_page.decode("utf-8")

        # If not cached, fetch the page, cache it and set expiration
        page_content = fn(url)
        redis_client.setex(url, 10, page_content)
        return page_content
    return wrapper


@count_and_cache
def get_page(url: str) -> str:
    """Fetch the content of the given URL and return it"""
    response = requests.get(url)
    return response.text


# Testing the functionality with a slow URL to simulate caching
if __name__ == "__main__":
    # Use the slowwly URL to simulate slow response
    url =
    "http://slowwly.robertomurray.co.uk/delay/1000/url/http://example.com"
    # Access the page multiple times
    print(get_page(url))  # Fetch and cache the page content
    time.sleep(1)
    print(get_page(url))  # Fetch from cache after 1 second
    time.sleep(9)
    print(get_page(url))  # Cache expires, fetch again
