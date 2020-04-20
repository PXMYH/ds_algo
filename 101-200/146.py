# 146. LRU Cache
# Medium

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.item_count = 0

    def get(self, key: int) -> int:
        print(f"accessing key {key}")
        if not key in self.cache.keys():
            print(f"key {key} is not in cache")
            return -1

        self.cache.move_to_end(key,last=False)
        print(f"put {key} at the start of cache")
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # check if capacity is exceeded, if yes, pop the first
        print(f"trying to put {value} into cache at {key}")
        print(f'current capacity {self.capacity}, current items count in cache {self.item_count}')

        # key already exist in cache, update
        if key in self.cache.keys():
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)

        # key doesn't exist in cache
        else:
            if self.item_count >= self.capacity:
                print(f"cache is full, evicting the least used item")
                self.cache.popitem(last=True)
                self.item_count -= 1

            # if no then add to the ordered dictionary, then increment item number
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
            self.item_count += 1

        print(f"final view of cache {self.cache}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# driver code
cache = LRUCache(2)

# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)
# cache.put(3, 3)
# cache.get(2)
# cache.put(4, 4)
# cache.get(1)
# cache.get(3)
# cache.get(4)

cache.get(2)
cache.put(2, 6)
cache.get(1)
cache.put(1, 5)
cache.put(1, 2)
cache.get(1)
cache.get(2)

# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]


# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]


# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
