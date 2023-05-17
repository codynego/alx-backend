#!/usr/bin/env python3

"""
Basic dictionary
"""
from base_caching import BaseCaching


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
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
