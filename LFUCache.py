"""
460. LFU Cache - Explanation


Description
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input: ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
Explanation:
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1); // cache=[1,_], cnt(1)=1
lfu.put(2, 2); // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1); // return 1
// cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3); // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
// cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2); // return -1 (not found)
lfu.get(3); // return 3
// cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4); // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
// cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1); // return -1 (not found)
lfu.get(3); // return 3
// cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4); // return 4
// cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:

1 <= capacity <= 10,000.
0 <= key <= 100,000
0 <= value <= 1,000,000,000
At most 200,000 calls will be made to get and put.
"""


from collections import defaultdict

# Node class
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Doubly linkedlist
class DLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0, self.left)
        self.left.next = self.right
        self.map = {}
    
    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = Node(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.map.pop(val, None)
    
    def popleft(self):
        res = self.left.next.val
        self.pop(res)
        return res
    

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.lfuCnt = 0
        self.mapKeyVal = {}                       # Map key -> val
        self.mapKeyCnt = defaultdict(int)         # Map key -> count
        self.KeyLList = defaultdict(DLinkedList)  # Map count of key -> linkedlist
    
    def counter(self, key):
        cnt = self.mapKeyCnt[key]
        self.mapKeyCnt[key] += 1
        self.KeyLList[cnt].pop(key)
        self.KeyLList[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.KeyLList[cnt].length() == 0:
            self.lfuCnt += 1
        
    
    def get(self, key):
        if key not in self.mapKeyVal:
            return -1
        self.counter(key)
        return self.mapKeyVal[key]

    def put(self, key, val):
        if self.cap == 0:
            return

        if key not in self.mapKeyVal and len(self.mapKeyVal) == self.cap:
            res = self.KeyLList[self.lfuCnt].popleft()
            self.mapKeyVal.pop(res)
            self.mapKeyCnt.pop(res)

        self.mapKeyVal[key] = val
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.mapKeyCnt[key])



# This LFU (Least Frequently Used) problem is LRU (Least Recently Used) problem with 
# added hashmap or dictionary and make it more challanging, using doubly linkedlist 
# gonna make put and get operation to be O(1) time complexity

ops = ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
args = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
output = [None, None, 1, None, -1, 3, None, -1, 3, 4]

lfu = LFUCache(2)
res = []
for i in range(len(ops)):
    res.append(getattr(lfu, ops[i])(*args[i]))
print(res)
print(output)