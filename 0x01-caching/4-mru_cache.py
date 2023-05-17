#!/usr/bin/env python3
"""
MRU Caching
Most Recently Used
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching class
    """
    def __init__(self):
        """
        initializing the instances
        """
        self.age_bits = {}
        self.age = 0
        super().__init__()  # calling the parent class

    def put(self, key, item):
        """
        adding an item to the cache

        Args:
            key (str): the key
            item (str or int): the value
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        elif len(self.cache_data) >= self.MAX_ITEMS:
            smallest_value = max(self.age_bits, key=self.age_bits.get)
            del self.cache_data[smallest_value]
            del self.age_bits[smallest_value]
            print(f"DISCARD: {smallest_value}")
        self.cache_data[key] = item
        if key in self.age_bits:
            pass
        else:
            self.age_bits[key] = self.age
        self.age += 1

    def get(self, key):
        """
        implemented get method that gets a value from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.age_bits[key] = self.age
        self.age += 1
        return self.cache_data[key]
