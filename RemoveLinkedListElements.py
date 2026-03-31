"""
203. Remove Linked List Elements

Solved
Easy
Topics
premium lock icon
Companies

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:
[1] -> [2] -> [6] -> [3] -> [4] -> [5] -> [6]            -> delete 6
                      |
       [1] -> [2] -> [3] -> [4] -> [5]
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]



Example 2:
Input: head = [], val = 1
Output: []



Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy = head
        prev, cur = dummy, head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return dummy.next
    

ll = [1,2,6,3,4,5,6]
val = 6
output = [1,2,3,4,5]

head = ListNode()
cur = head
for i in range(len(ll)):
    cur.next = ListNode(ll[i])
    cur = cur.next

s = Solution()
newHead = s.removeElements(head, val)

res = []
newCur = newHead
while newCur:
    res.append(newCur.val)
    newCur = newCur.next
print(res)
print(output)