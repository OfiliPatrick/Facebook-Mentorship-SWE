import collections

class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return - 1
            
        else:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]


    def add(self, key, val):
        if len(self.cache) == self.size:
            self.cache.popitem(last=True)

        self.cache[key] = val
        self.cache.move_to_end(key)

            
newLRUCache = 
        
            

cache = collections.OrderedDict()

cache[1] = 2
cache[3] = 4
cache[5] = 6
# cache.move_to_end(3, last=False)

cache.popitem(last=True)
print(cache)