"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""

class LinkedList:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hash = [LinkedList() for i in range(10**3)]


    def put(self, key, value):
        cur = self.hash[key % len(self.hash)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                # Return it immediately so we not gonna add more to a different key
                return
            cur = cur.next
        cur.next = LinkedList(key, value)


    def get(self, key):
        cur = self.hash[key % len(self.hash)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1


    def remove(self, key):
        cur = self.hash[key % len(self.hash)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next



com = ["put", "put", "get", "get", "put", "get", "remove", "get"]
val = [[1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
output = [None, None, 1, -1, None, 1, None, -1]

res = []
mhm = MyHashMap()
for i in range(len(com)):
    # Convert the list to a touple so we can destructure it because the input 
    # arguments are varies
    arg = tuple(val[i])
    # Using getattr do dynamically calling a method
    # Destruture using *arg 
    res.append(getattr(mhm, com[i])(*arg))

print(res)
print(output)