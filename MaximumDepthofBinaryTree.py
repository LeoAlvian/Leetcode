"""
104. Maximum Depth of Binary Tree

Solved
Easy
Topics
premium lock icon
Companies

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

            [3]         
         /       \            
       [9]       [20]            
                /     \           
              [15]    [7]  

Input: root = [3,9,20,null,null,15,7]
Output: 3



Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

class Solution:

    # Solve Iteratively with time: O(n) and space: O(n)
    # This algorithm is 1ms on leetcode

    def maxDepth(self, root):
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return res
   

    # Solve using BFS with time: O(n) and space: O(n)
    # This algorithm is faster on leetcode with 0ms
    
    def maxDepthBFS(self, root):
        if not root:
            return 0

        res = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1

        return res



#         [3]         
#      /       \            
#    [9]       [20]            
#             /     \           
#           [15]    [7] 


li = [3,9,20,None,None,15,7]
output = 3

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()

res = s.maxDepth(root)
res2 = s.maxDepthBFS(root)

print(res)
print(res2)
print(output)