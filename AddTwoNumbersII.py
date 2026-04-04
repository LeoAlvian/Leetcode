"""
445. Add Two Numbers II

Solved
Medium
Topics
premium lock icon
Companies

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:
[7] -> [2] -> [4] -> [3]
       [5] -> [6] -> [4]
------------------------- +
[7] -> [8] -> [0] -> [7]

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]



Example 2:
       [2] -> [4] -> [3]
       [5] -> [6] -> [4]
------------------------- +
       [8] -> [0] -> [7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]



Example 3:
                     [0]
                     [0]
------------------------- +
                     [0]

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?
"""



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Helper function to reverse linked list
        def reverseLink(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
            
        # Reverse both linked list
        l1 = reverseLink(l1)
        l2 = reverseLink(l2)
        head = None
        carry = 0

        # Calculate the addition and consider an edge case where the lenght of linked list
        # are not the same
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head
            head = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head



l1 = [7,2,4,3]
l2 = [5,6,4]
output = [7,8,0,7]

head1 = ListNode()
head2 = ListNode()
cur1 = head1
cur2 = head2
for el in l1:
    cur1.next = ListNode(el)
    cur1 = cur1.next
for el in l2:
    cur2.next = ListNode(el)
    cur2 = cur2.next

s = Solution()
head = s.addTwoNumbers(head1.next, head2.next)

res = []
cur = head
while cur:
    res.append(cur.val)
    cur = cur.next

print(res)
print(output)