class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)
        self.lru_cache = []
        self.lru_size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_cache.remove(key)
            self.lru_cache.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.lru_size < self.capacity:
                self.lru_cache.append(key)
                self.lru_size += 1
            else:
                self.cache.pop(self.lru_cache[0])
                self.lru_cache.remove(self.lru_cache[0])
                self.lru_cache.append(key)
        else:
            self.lru_cache.remove(key)
            self.lru_cache.append(key)
           

        self.cache[key] = value
