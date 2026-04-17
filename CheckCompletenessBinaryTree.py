"""
958. Check Completeness of a Binary Tree

Solved
Medium
Topics
premium lock icon
Companies

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:
                  [1]
                /     \
             [2]       [3]
            /   \     / 
          [4]   [5] [6]
            
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.



Example 2:

                  [1]
                /     \
             [2]       [3]
            /   \         \ 
          [4]   [5]        [7]

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""


from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root):
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False
        
        return True



#           [1]
#         /     \
#      [2]       [3]
#     /   \     / 
#   [4]   [5] [6]
            
arr = [1,2,3,4,5,6]
output = True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s = Solution()
res = s.isCompleteTree(root)

print(res)
print(output)