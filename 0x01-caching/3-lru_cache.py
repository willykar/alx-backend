#!/usr/bin/python3
""" Iru_cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defines A LRUCache class
    that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LRUCache """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """ Put method that assigns the item to
        the dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Get method that
        Returns the value associated with the given key """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
