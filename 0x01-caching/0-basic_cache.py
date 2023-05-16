#!/usr/bin/env python3

"""
Basic dictionary
"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that overrides
    the put and get method in the base class (BaseCaching)
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
