"""
199. Binary Tree Right Side View

Solved
Medium
Topics
premium lock icon
Companies

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:

                 [1]  <----------------
               /     \
             [2]      [3] <------------
                \        \ 
                [5]      [4] <---------
            

                

Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:

                 [1]  <-----------------
               /    \
             [2]     [3]  <-------------
            /   
         [4]  <-------------------------   
        /  
      [5]  <----------------------------


            

      

Example 3:

Input: root = [3,9,20,null,null,15,7]
Output: [3,20,7,5]
Explanation:

                 [3]  <-------------------
               /     \
             [9]      [20]  <-------------
            /   \    /    \
         [0]    [4] [15]   [7]  <---------
               /  \
             [3]  [5]  <------------------



Example 4:

Input: root = [1,null,3]
Output: [1,3]


Example 5:

Input: root = []
Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""



class Tree:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None



# Solving it using BFS with time: O(n) and space: O(h); where n is the number of node and 
# h is the hight of the tree

from collections import deque

class Solution:
    def rightSideView(self, root):
        res = []
        q = deque([root])

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res



    #          [3]  <-------------------
    #        /     \
    #      [9]      [20]  <-------------
    #     /   \    /    \
    #  [0]    [4] [15]   [7]  <---------
    #        /  \
    #      [3]  [5]  <------------------


root = [3,9,20,None,None,15,7]
output = [3,20,7,5]

root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.left.left = Tree(0)
root.left.right = Tree(4)
root.left.right.left = Tree(3)
root.left.right.right = Tree(5)
root.right.left = Tree(15)
root.right.right = Tree(7)

s = Solution()

res = s.rightSideView(root)

print(res)
print(output)