#This class implements a CPU cache as outlined in the project promt, includng a replacement policy of LRU (least recently used). 


import collections

cache_size = 16

class Cache:

    def __init__(self):
        self.cache = collections.OrderedDict()
    
    # By removing and reinserting the value to the cache, we keep track of how recently information has been used. 
    def search_cache(self, address):
        if address in self.cache:
            value = self.cache.pop(address)
            self.cache[address] = value
            return value
        else:
            return None 
    
    #Replacement policy- if the cache is ful, we remove the oldest item (FIFO/LRU)
    def write_cache(self, address, value):
        if len(self.cache) > cache_size:
            self.cache.popitem(last=False)
        self.cache[address] = value
                              