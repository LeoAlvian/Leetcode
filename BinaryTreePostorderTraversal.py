"""
145. Binary Tree Postorder Traversal - Explanation


Description
You are given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [4,5,2,6,7,3,1]



Example 2:

Input: root = [1,2,3,null,4,5,null]
Output: [4,2,5,3,1]



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
    def PostorderTraversal(self, root):
        stack = [root]
        visited = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visited.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        
        return res


list = [1,2,3,4,5,6,7]
output = [4,5,2,6,7,3,1]
s = Solution()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = s.PostorderTraversal(root)

print(res)
print(output)