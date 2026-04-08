"""
617. Merge Two Binary Trees

Solved
Easy
Topics
premium lock icon
Companies

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]




Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
 

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, r1, r2):
        if not r1 and not r2:
            return None
        
        v1 = r1.val if r1 else 0
        v2 = r2.val if r2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(r1.left if r1 else None, r2.left if r2 else None)
        root.right = self.mergeTrees(r1.right if r1 else None, r2.right if r2 else None)
        return root


    # Using BFS
    def levelOrderTraversal(self, root):
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
            



#            [1]
#         /       \
#       [3]       [2]
#     /    
#   [5]    
list1 = [1,3,2,5]
#            [2]
#         /       \
#       [1]       [3]
#           \       \
#           [4]     [7]
list2 = [2,1,3,None,4,None,7]
#            [3]
#         /       \
#       [4]       [5]
#     /     \         \
#   [5]    [4]        [7]
output = [3,4,5,5,4,None,7]

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

s = Solution()
newRoot = s.mergeTrees(root1, root2)
res = s.levelOrderTraversal(newRoot)

print(res)
print(output)