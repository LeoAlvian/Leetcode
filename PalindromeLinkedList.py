"""
234. Palindrome Linked List

Solved
Easy
Topics
premium lock icon
Companies

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:
 [1] -> [2] -> [2] -> [1]
Input: head = [1,2,2,1]
Output: true




Example 2:
[1] -> [2]
Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        fast = head
        slow = head

        # Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse middle to end
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Find Palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



ll = [1,2,2,1]
output = True

head = ListNode()
cur = head
for el in ll:
    cur.next = ListNode(el)
    cur = cur.next

s = Solution()
print(s.isPalindrome(head.next))
print(output)