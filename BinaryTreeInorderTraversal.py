"""
94. Binary Tree Inorder Traversal

You are given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [4,2,5,1,6,3,7]



Example 2:

Input: root = [1,2,3,null,4,5,null]
Output: [2,4,1,5,3]



Example 3:
Input: root = []
Output: []


Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # This using recursive function which is trivial, but we are requested if
    # we can do it iteratively 
    def inorderTraversal(self, root):
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res
    
    # Iterative solution
    # Using stack to store the node that we currently in

    def inorderTravIterative(self, root):
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res





list = [1,2,3,4,5,6,7]
output = [4,2,5,1,6,3,7]

list = [1,2,3,None,4,5,None]
output = [2,4,1,5,3]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

s = Solution()
res = s.inorderTraversal(root)
res2 = s.inorderTravIterative(root)
print('Using recursive:', res)
print('Using iterative:', res2)
print('Output:', output)