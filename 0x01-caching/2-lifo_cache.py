#!/usr/bin/usr python3

"""
Lifo implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    last in first out caching system
    that inherited from BaseCaching
    """
    def __init__(self):
        """
        initializing the instances
        """
        super().__init__()  # the parent class

    def put(self, key, item):
        """
        a method that adds an item to a cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            print(f"DISCARD: {key}")

        elif len(self.cache_data) >= self.MAX_ITEMS:
            cache_dict = self.cache_data.popitem()
            print(f"DISCARD: {cache_dict[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
        a method that get or fetch an item from a cache
        """
        if key is None or key not in self.cache_data:
            return None
        return (self.cache_data[key])
