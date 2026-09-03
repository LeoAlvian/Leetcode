"""
19. Remove Nth Node From End of List

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
                          2      1
    [1] -> [2] -> [3] -> [4] -> [5]   : n = 2

    [1] -> [2] -> [3] -> [5]   : n = 2


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:

Input: head = [1], n = 1
Output: []


Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next



def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    l = dummy
    r = head

    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        r = r.next
        l = l.next

    l.next = l.next.next
    return dummy.next


li = [1,2,3,4,5]
n = 2
output = [1,2,3,5]

dummy = ListNode(0)
cur = dummy

for l in li:
    cur.next = ListNode(l)
    cur = cur.next

newHead = removeNthFromEnd(dummy.next, n)
cur2 = newHead
res = []

while cur2:
    res.append(cur2.val)
    cur2 = cur2.next

print(res)
print(output)