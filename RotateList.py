"""
61. Rotate List

Solved
Medium
Topics
premium lock icon
Companies

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
           [1] -> [2] -> [3] -> [4] -> [5]
Rotate 1 : [5] -> [1] -> [2] -> [3] -> [4] 
Rotate 2 : [4] -> [5] -> [1] -> [2] -> [3]

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]



Example 2:
           [0] -> [1] -> [2]
Rotate 1 : [2] -> [0] -> [1] 
Rotate 2 : [1] -> [2] -> [0] 
Rotate 3 : [0] -> [1] -> [2]  
Rotate 4 : [2] -> [0] -> [1] 

Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        cur =  head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead



listl = [1,2,3,4,5]
k = 2
output = [4,5,1,2,3]

head = ListNode()
cur = head
for el in listl:
    cur.next = ListNode(el)
    cur = cur.next

s = Solution()
newHead = s.rotateRight(head.next, k)

res = []
cur2 = newHead
while cur2:
    res.append(cur2.val)
    cur2 = cur2.next

print(res)
print(output)