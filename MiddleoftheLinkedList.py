"""
876. Middle of the Linked List

Solved
Easy
Topics
premium lock icon
Companies

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.



Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def printll(self, head):
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next
        
        return res


list = [1,2,3,4,5,6]
output = [4,5,6]

head = LinkedList()
cur = head
for l in list:
    cur.next = LinkedList(l)
    cur = cur.next

s = Solution()
mid = s.middleNode(head.next)
res = s.printll(mid)

print(res)
print(output)