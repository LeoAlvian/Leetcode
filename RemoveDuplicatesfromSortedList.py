"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]


Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Use Linked List data structure to store the data
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        cur = head
        # loop through the linked list
        while cur:
            # loop through the linked list value that is the same and deleting it
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        
        # we must return the head 
        return head




head = [1,1,2,3,3,4,4,4,4]
output = [1,2,3,4]
cur = ListNode()
# we must assign cur to cur2 so we didn't change the head of the list
cur2 = cur
for h in head:
    cur2.next = ListNode(h)
    cur2 = cur2.next
s = Solution()
# we assign new head to add linked list to arr and print it
newHead = s.deleteDuplicates(cur)
res = []
while newHead.next:
    res.append(newHead.next.val)
    newHead = newHead.next
print(res)
print(output)