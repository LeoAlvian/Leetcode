"""
21. Merge Two Sorted Lists

Solved
Easy
Topics
premium lock icon
Companies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]



Example 2:

Input: list1 = [], list2 = []
Output: []



Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Node class
class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return dummy.next




list1 = [1,2,4]
list2 = [1,3,4]
output = [1,1,2,3,4,4]

head1 = ListNode()
head2 = ListNode()

cur1 = head1
cur2 = head2

for l1 in list1:
    cur1.next = ListNode(l1)
    cur1 = cur1.next

for l2 in list2:
    cur2.next = ListNode(l2)
    cur2 = cur2.next

s = Solution()

head = s.mergeTwoLists(head1.next, head2.next)
cur = head
res = []

while cur:
    res.append(cur.val)
    cur = cur.next

print(res)
print(output)