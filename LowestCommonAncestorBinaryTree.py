"""
236. Lowest Common Ancestor of a Binary Tree

Solved
Medium
Topics
premium lock icon
Companies

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
                 [3]
               /     \
             [5]      [1]
            /   \    /    \
         [6]    [2] [0]   [8]
               /  \
             [7]  [4]

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.



Example 2:
                 [3]
               /     \
             [5]      [1]
            /   \    /    \
         [6]    [2] [0]   [8]
               /  \
             [7]  [4]

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.



Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Using BFS
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {root: None}
        queue = deque([root])
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]

        return q
        


#                  [3]
#                /     \
#              [5]      [1]
#             /   \    /    \
#          [6]    [2] [0]   [8]
#                /  \
#              [7]  [4]
lists = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 4
output = 5


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left 
q = root.left.right.right

s = Solution()

# Commont fit fall is p and q is supposed to be a node not an integer
res = s.lowestCommonAncestor(root, p, q)

print(res.val)
print(output)