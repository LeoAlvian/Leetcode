"""
143. Reorder List

Solved
Medium
Topics
premium lock icon
Companies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]



Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# List Node class

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reorderList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    tail = slow.next
    prev = slow.next = None
    while tail:
        tmp = tail.next
        tail.next = prev
        prev = tail
        tail = tmp

    tail = prev
    cur = head
    while tail:
        tmp1, tmp2 = cur.next, tail.next
        cur.next = tail
        tail.next = tmp1
        cur, tail = tmp1, tmp2

    return head


li = [1,2,3,4,5]
output = [1,5,2,4,3]

head = ListNode()
cur = head

for l in li:
    cur.next = ListNode(l)
    cur = cur.next

newHead = reorderList(head.next)
cur = newHead
res = []

while cur:
    res.append(cur.val)
    cur = cur.next

print(res)
print(output)