"""
543. Diameter of Binary Tree

Solved
Easy
Topics
premium lock icon
Companies

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

            [1]
         /       \
       [2]       [3]
     /   \   
   [4]   [5]

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].



Example 2:

            [1]
                \
                [3]
              /     \   
            [4]      [5]
           /   \    /   \
         [6]   [7] [8]  [9]
   
Input: root = [1,2,3,4,5,6,7,8,9]
Output: 4



Example 3:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""



class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0

        def dfs(cur):
            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res




    #     [1]
    #         \
    #         [3]
    #       /     \   
    #     [4]      [5]
    #    /   \    /   \
    #  [6]   [7] [8]  [9]
   
li = [1,2,3,4,5,6,7,8,9]
output = 4

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

s = Solution()

res = s.diameterOfBinaryTree(root)

print(res)
print(output)