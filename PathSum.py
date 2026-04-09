"""
112. Path Sum

Solved
Easy
Topics
premium lock icon
Companies

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:
                [5]
              /     \
            [4]     [8]
           /       /   \
        [11]     [13]  [4]
       /   \             \
     [7]   [2]           [1]    

     5 -> 4 -> 11 -> 2 = 22
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.



Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.



Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)



#                 [5]
#               /     \
#             [4]     [8]
#            /       /   \
#         [11]     [13]  [4]
#        /   \             \
#      [7]   [2]           [1]  
list = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
output = True

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

s = Solution()
res = s.hasPathSum(root, targetSum)

print(res)
print(output)