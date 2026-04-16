"""
103. Binary Tree Zigzag Level Order Traversal

Solved
Medium
Topics
premium lock icon
Companies

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:

                  [3]
                /     \
              [9]      [20]
                       /   \    
                     [15]   [7]   

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]



Example 2:
Input: root = [1]
Output: [[1]]



Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if len(res) % 2:
                level.reverse()
            res.append(level)
        
        return res
        




#          [3]
#        /     \
#      [9]      [20]
#              /   \    
#            [15]   [7]   

arr = [3,9,20,None,None,15,7]
output = [[3],[20,9],[15,7]]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
res = s.zigzagLevelOrder(root)

print(res)
print(output)