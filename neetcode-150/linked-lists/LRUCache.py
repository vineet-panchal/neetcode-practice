# 146 - LRU Cache
# Leetcode Link: https://leetcode.com/problems/lru-cache/

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

'''

'''
Initial Thoughts
  - Design a data structure that supports LRU (Least Recently Used) cache operations.
  - Support get and put operations in O(1) average time.
Simplify the problem:
  - Use a hashmap for fast key lookup and a doubly linked list for order.
  - Evict least recently used item when capacity is exceeded.
Pattern Recognition: Straightforward solution
  - Use a list to track usage order and a dictionary for values.
  - O(n) time for updates, not optimal.
Pattern Recognition: Optimal solution
  - Use doubly linked list and hashmap for O(1) operations. 
  - Efficiently update usage order and handle evictions.
'''

import collections

class LRUCache:
    def __init__(self, capacity: 'int'):
        self.cache = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: 'int') -> 'int':
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # meaning end is the most recently used
        return self.cache.get(key)

    def put(self, key: 'int', value: 'int') -> 'None':
        if key not in self.cache:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.cache.popitem(last=False) # pop start position
        else:
            self.cache.pop(key)
        self.cache[key] = value # add to end of dict, meaning most recently used


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    print(lRUCache.get(1))    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))    # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))    # return -1 (not found)
    print(lRUCache.get(3))    # return 3
    print(lRUCache.get(4))    # return 4

    print("--- Additional tests ---")
    # Test with capacity 1
    cache1 = LRUCache(1)
    cache1.put(1, 1)
    print(cache1.get(1)) # expect 1
    cache1.put(2, 2)
    print(cache1.get(1)) # expect -1 (evicted)
    print(cache1.get(2)) # expect 2

    # Test updating existing key
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(1, 10)  # update key 1 value to 10
    print(cache2.get(1)) # expect 10
    cache2.put(3, 3)  # evict least recently used (key 2)
    print(cache2.get(2)) # expect -1

    # Test getting non-existent key
    cache3 = LRUCache(2)
    print(cache3.get(100)) # expect -1

    # Test eviction order with several puts
    cache4 = LRUCache(3)
    cache4.put(1, 1)
    cache4.put(2, 2)
    cache4.put(3, 3)
    cache4.get(1) # access key 1 making it recently used
    cache4.put(4, 4) # evict key 2 (least recently used)
    print(cache4.get(2)) # expect -1
    print(cache4.get(3)) # expect 3
    print(cache4.get(4)) # expect 4
    print(cache4.get(1)) # expect 1
