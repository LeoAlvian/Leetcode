"""
138. Copy List with Random Pointer

Solved
Medium
Topics
premium lock icon
Companies
Hint

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:

     ---------------------------------------
     |                                     |
     |               ----------------      |
     |               |              |      |
     |               |              v      v
    [7] -> [13] -> [11] -> [10] -> [1] -> None
     ^       |      ^       |       |
     |       |      |       |       |
     ---------      ---------       |
     ^                              |
     |                              |
     --------------------------------

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]



Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]



Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""



class ListNode:
    def __init__(self, val, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    oldToCopy = { None : None }

    cur = head
    while cur:
        copy = ListNode(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next

    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next

    return oldToCopy[head]



li = [[7,None],[13,0],[11,4],[10,2],[1,0]]
output = [[7,None],[13,0],[11,4],[10,2],[1,0]]

listDict = {}
dummy = ListNode(0)
cur = dummy
for i, l in enumerate(li):
    cur.next = ListNode(l[0], None, None)
    listDict[i] = cur.next
    cur = cur.next

print(listDict[1].val)

cur2 = dummy.next
i = 0
while cur2:
    print(li[i][1])
    cur2.random = listDict[i]
    cur2 = cur2.next
    i += 1


newHead = copyRandomList(dummy.next)

newCur = newHead
res = []
while newCur:
    res.append([newCur.val, newCur.random.val])
    newCur = newCur.next

print(res)
print(output)
