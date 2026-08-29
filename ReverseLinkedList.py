"""
206. Reverse Linked List

Solved
Easy
Topics
premium lock icon
Companies

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]



Example 2:

Input: head = [1,2]
Output: [2,1]



Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

# Using Iterative solution with two pointers

class ReverseLL:
    # def __init__(self):
    #     self.head = None

    # def addNode(self, val):
    #     if not self.head:
    #         self.head.next = ListNode(val)
    #         return

    #     cur = self.head
    #     while cur.next:
    #         cur = cur.next
    #     cur.next = ListNode(val)
        


    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


ls = [1,2,3,4,5]
output = [5,4,3,2,1]

head = ListNode()
cur = head
for h in ls:
    cur.next = ListNode(h)
    cur = cur.next

rll = ReverseLL()
newHead = rll.reverseList(head)

res = []

while newHead.next:
    res.append(newHead.val)
    newHead = newHead.next

print(res)
print(output)