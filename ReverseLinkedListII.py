"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]


Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 
"""

class LinkedList():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head, l, r):
        dummyNode = LinkedList(0, head)

        prevLeft, cur = dummyNode, head
        for i in range(l - 1):
            prevLeft, cur = cur, cur.next
        
        prev = None
        for i in range(r - l + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        prevLeft.next.next = cur
        prevLeft.next = prev
    
        return dummyNode.next


list = [1,2,3,4,5]
left = 2
right = 4
output = [1,4,3,2,5]

cur = LinkedList()
# we must assign cur to cur2 so we didn't change the head of the list
cur2 = cur
for h in list:
    cur2.next = LinkedList(h)
    cur2 = cur2.next
s = Solution()
newHead = s.reverseLinkedList(cur.next, left, right)
res = []
while newHead:
    res.append(newHead.val)
    newHead = newHead.next
print(res)
print(output)