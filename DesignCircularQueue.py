"""
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true   if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""


# We are using Singly LinkedList data structure to solve this problems, we can also 
# use Doubly LinkedList we gonna use less if statement but more also adding prev to 
# the LinkedList object
#
# Ex
#
# Initiation took O(n) time complexity
# k = 3
#     []    ->     []     ->      []
# head/tail
# 
# enQueue(1)
#    [1]    ->     []      ->      []    -> return True because we can add to the list
# head/tail
#
# enQueue(2)
#    [1]    ->     [2]     ->      []    -> return True because we can add to the list
#    head          tail
#
# enQueue(3)
#    [1]    ->     [2]     ->      [3]   -> return True because we can add to the list
#    head                          tail
#
# enQueue(4)
#    [1]    ->     [2]     ->      [3]   -> return False, we can't add to the list
#    head                          tail
#
# Rear()/tail   -> return 3 because tail.val is 3
#
# isFull()      -> return True because the list is full
#
# deQueue()     -> return True because we can delete from list
#    []    ->     [2]     ->      [3]   -> return False, we can't add to the list
#                 head            tail
#
# enQueue(4)
#    [4]    ->     [2]     ->      [3]   -> return True, we can add to the list
#    tail          head        
# 
# Rear()/tail    -> return 4 because tail.val is 4
#      

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self, k):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0


    def enQueue(self, value):
        if self.isFull():
            return False
        
        if self.count == 0:
            self.head = LinkedList(value)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(value)
            self.tail = self.tail.next
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1
        return True


    def Front(self):
        if self.isEmpty():
            return -1
        self.head.val


    def Rear(self):
        if self.isEmpty():
            return -1
        return self.tail.val


    def isFull(self):
        return self.capacity == self.count


    def isEmpty(self):
        return self.count == 0


operations = ["enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
args = [[1], [2], [3], [4], [], [], [], [4], []]
k = 3
output = [True, True, True, False, 3, True, True, True, 4]

res = []
s = Solution(k)
for i in range(len(operations)):
    res.append(getattr(s, operations[i])(*args[i]))
print(res)
print(output)