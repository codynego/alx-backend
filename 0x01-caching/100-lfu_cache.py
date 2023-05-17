#!/usr/bin/env python3
"""
LFU Caching
Least Frequently Used
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching class
    """
    def __init__(self):
        """
        initializing the instances
        """
        self.age_bits = {}
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
            smallest_value = min(self.age_bits, key=self.age_bits.get)
            del self.cache_data[smallest_value]
            del self.age_bits[smallest_value]
            print(f"DISCARD: {smallest_value}")
        self.cache_data[key] = item
        if key in self.age_bits:
            pass
        else:
            self.age_bits[key] = 0
        print(self.age_bits)

    def get(self, key):
        """
        implemented get method that gets a value from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.age_bits[key] += 1
        return self.cache_data[key]
