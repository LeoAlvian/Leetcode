"""
2130. Maximum Twin Sum of a Linked List

Solved
Medium
Topics
premium lock icon
Companies
Hint

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:
          [5] -> [4] -> [2] -> [1]
                  4  +   2           = 6
           5         +          1    = 6
Max sum = 6
return Max sum

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 




Example 2:
          [4] -> [2] -> [2] -> [3]
                  2  +   2           = 4
           4         +          3    = 7
Max sum = 7
return Max sum

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 




Example 3:
                 [1] -> [100000]
                  1  +   100000      = 100001
Max sum = 100001
return Max sum

Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

# We traverse through the linked list using fast and slow pointer to find the middle part,
# when the fast reach the end the slow will right after the middle 
# While we traverse we gonna reverse the slow pointer to point at the opposite direction,
# We gonna use prev to reverse while traverse through slow pointer
# So the linked list is goes from
#          [4] -> [2] -> [2] -> [3]
# To this
#          [4] <- [2]    [2] -> [3]
#                prev    slow
# Now we traverse through slow and prev at the same time and add them, find max and store it
# in res variable  
#          [4] <- [2]    [2] -> [3]
#                  2  +   2           = 4
#           4         +          3    = 7
# Max res = max(4, 7)
# return res = 7

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:
    def pairSum(self, head):
        fast, slow = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res



ll = [4,2,2,3]
output = 7
head = LinkedList(ll[0])
cur = head
for i in range(1, len(ll)):
    cur.next = LinkedList(ll[i])
    cur = cur.next

s = Solution()
res = s.pairSum(head)

print(res)
print(output)