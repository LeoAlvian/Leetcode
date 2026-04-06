"""
147. Insertion Sort List

Solved
Medium
Topics
premium lock icon
Companies

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]



Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
"""



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            
            tmp = dummy
            while cur.val >= tmp.next.val:
                tmp = tmp.next
            
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        
        return dummy.next


ll = [4,2,1,3]
output = [1,2,3,4]

head = ListNode()
cur = head
for el in ll:
    cur.next = ListNode(el)
    cur = cur.next

res = []
s = Solution()
newHead = s.insertionSortList(head.next)
newCur = newHead
while newCur:
    res.append(newCur.val)
    newCur = newCur.next

print(res)
print(output)