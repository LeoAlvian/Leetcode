"""
144. Binary Tree Preorder Traversal

Description
You are given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,2,4,5,3,6,7]



Example 2:

Input: root = [1,2,3,null,4,5,null]
Output: [1,2,4,3,5]



Example 3:

Input: root = []
Output: []



Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        
        return res



list = [1,2,3,4,5,6,7]
output = [1,2,4,5,3,6,7]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

s = Solution()
res = s.preorderTraversal(root)
print(res)
print(output)