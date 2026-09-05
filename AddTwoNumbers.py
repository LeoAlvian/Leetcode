"""
2. Add Two Numbers

Solved
Medium
Topics
premium lock icon
Companies

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

    [2] -> [4] -> [3]
    [5] -> [6] -> [4]
    ----------------- +
    [7] -> [0] -> [8]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.



Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]



Example 3:

    [9] -> [9] -> [9] -> [9] -> [9] -> [9] -> [9]
    [9] -> [9] -> [9] -> [9] 
    --------------------------------------------- +
    [8] -> [9] -> [9] -> [9] -> [0] -> [0] -> [0] -> [1]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # Adding two number with the carry
        val = v1 + v2 + carry

        # Handle the carry
        carry = val // 10
        val %= 10

        # Adding the value to the linked list and update the pointer
        cur.next = ListNode(val)
        cur = cur.next

        # Update l1 and l2 pointer
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next




def createListNode(cur, listInt):
    for l in listInt:
        cur.next = ListNode(l)
        cur = cur.next


head1 = [9,9,9,9,9,9,9]
head2 = [9,9,9,9]
output = [8,9,9,9,0,0,0,1]

dummy = ListNode()
dummy2 = ListNode()

cur1, cur2 = dummy, dummy2
createListNode(cur1, head1)
createListNode(cur2, head2)

newHead = addTwoNumbers(dummy.next, dummy2.next)
res = []

while newHead:
    res.append(newHead.val)
    newHead = newHead.next

print(res)
print(output)