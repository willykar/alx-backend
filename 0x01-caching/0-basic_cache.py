#!/usr/bin/python3
""" basic_cache module """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Define BasicCache class that inherits from
    BaseCaching
    """

    def put(self, key, item):
        """ A put method that
        assigns the item to the dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ A get method that
        returns the value associated with the given key
        """
        return self.cache_data.get(key)
