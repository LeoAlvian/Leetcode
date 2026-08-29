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

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


    def reverseListII(self, head):
        def dfs(head):
            if not head or not head.next:
                return head

            new_head = dfs(head.next)

            head.next.next = head
            head.next = None

            return new_head

        return dfs(head)


ls = [1,2,3,4,5]
output = [5,4,3,2,1]

head = ListNode()
head2 = ListNode()
cur = head
cur2 = head2
for h in ls:
    cur.next = ListNode(h)
    cur2.next = ListNode(h)
    cur = cur.next
    cur2 = cur2.next

rll = ReverseLL()

newHead = rll.reverseList(head)
newHead2 = rll.reverseListII(head2)

res = []
res2 = []

while newHead.next:
    res.append(newHead.val)
    newHead = newHead.next

while newHead2.next:
    res2.append(newHead2.val)
    newHead2 = newHead2.next

print(res)
print(res2)
print(output)