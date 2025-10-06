"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""


class LinkedList:
    def __init__(self, key):
        self.key = key 
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [LinkedList(0) for i in range(10**4)]


    def add(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = LinkedList(key)


    def remove(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


    def contains(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


com = ["add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
val = [[1], [2], [1], [3], [2], [2], [2], [2]]


res = []
mhs = MyHashSet()
# mhs.add(1)
# mhs.add(2)
# res.append(mhs.contains(1))
# res.append(mhs.contains(3))
# mhs.add(2)
# res.append(mhs.contains(2))
# mhs.remove(2)
# res.append(mhs.contains(2))

for i in range(len(com)):
    out = getattr(mhs, com[i])(val[i][0])
    res.append(out)

output = [None, None, True, False, None, True, None, False]
print(res)
print('output == res', output == res)