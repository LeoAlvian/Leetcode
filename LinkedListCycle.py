"""
141. Linked List Cycle

Solved
Easy
Topics
premium lock icon
Companies

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).



Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.



Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


# Node class
class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


# Using Floyd's Tortoise & Here algorithm to find a loop with time: O(n) and space: O(1)

def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



li = [3,2,0,-4]
pos = 1
output = True

# Creating a linked list
head = ListNode()
tail  = head 
for l in li:
    tail.next = ListNode(l)
    tail = tail.next

# Create a loop in a linked list
cur = head
while pos:
    cur = cur.next
    pos -= 1
tail.next = cur

res = hasCycle(head.next)

print(res)
print(output)