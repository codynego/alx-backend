#!/usr/bin/env python3
"""
Fifo Caching
"""

from BaseCaching import BaseCaching


class FIFOCache(BaseCaching):
    """
    fifo caching inherited from BaseCaching
    """
    def __init__(self):
        """
        initializing the instances
        """
        super().__init__()  # call the super class

    def put(self, key, item):
        """
        put a value into cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            dict_list = list(self.cache_data.items())
            first_item = dict_list.pop(0)
            self.cache_data = dict(dict_list)
            print(f"DISCARD: {first_item[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
        get a value from a cache using its key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
