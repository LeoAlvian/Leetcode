"""
102. Binary Tree Level Order Traversal

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

                 [3]
               /     \
             [9]      [20]
            /   \    /    \
         [0]    [4] [15]   [7]
               /  \
             [3]  [5]

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]



Example 2:

                 [6]
               /     \
             [2]      [8]
            /   \    /    \
         [0]    [4] [7]   [9]
               /  \
             [3]  [5]

Input: root = [6,2,8,0,4,7,9,null,null,3,5]
Output: [[6], [2,8], [0,4,7,9], [3,5]]



             
Example 3:

Input: root = [1]
Output: [[1]]


Example 4:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""



class Tree:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None



from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res




        #          [6]
        #        /     \
        #      [2]      [8]
        #     /   \    /    \
        #  [0]    [4] [7]   [9]
        #        /  \
        #      [3]  [5]

li = [6,2,8,0,4,7,9,None,None,3,5]
output = [[6], [2,8], [0,4,7,9], [3,5]]

root = Tree(6)
root.left = Tree(2)
root.right = Tree(8)
root.left.left = Tree(0)
root.left.right = Tree(4)
root.left.right.left = Tree(3)
root.left.right.right = Tree(5)
root.right.left = Tree(7)
root.right.right = Tree(9)

s = Solution()

res = s.levelOrder(root)

print(res)
print(output)