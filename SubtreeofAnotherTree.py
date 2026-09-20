"""
572. Subtree of Another Tree

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:

            root                subRoot
            [3]                   [4]
          /     \               /     \
        [4]      [5]         [1]      [2]
      /    \                 
    [1]    [2]             

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true



Example 2:

           root                 subRoot
            [3]                   [4]
          /     \               /     \
        [4]      [5]         [1]      [2]
      /    \                 
    [1]    [2]   
          /
        [0]

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""



class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSame(self, root, sub):
        if not root and not sub:
            return True
        if root and sub and root.val == sub.val:
            return True
        return False





    #         root                subRoot
    #         [3]                   [4]
    #       /     \               /     \
    #     [4]      [5]         [1]      [2]
    #   /    \                 
    # [1]    [2]             

li1 = [3,4,5,1,2]
li2 = [4,1,2]
output = True

root = Tree(3)
root.left = Tree(4)
root.right = Tree(5)
root.left.left = Tree(1)
root.left.right = Tree(2)

subTree = Tree(4)
subTree.left = Tree(1)
subTree.right = Tree(2)

s = Solution()

res = s.isSubtree(root,subTree)

print(res)
print(output)