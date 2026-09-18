"""
100. Same Tree

Solved
Easy
Topics
premium lock icon
Companies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:
              p              q  
             [1]            [1]
           /     \        /     \
        [2]      [3]    [2]     [3]

Input: p = [1,2,3], q = [1,2,3]
Output: true



Example 2:
                 p                     q
                [3]                   [3]
              /     \               /     \
            [9]      [20]         [9]      [20]
                    /    \                 /    \
                 [15]    [7]             [15]    [7]

Input: p = [3,9,20,null,null,15,7], q = [3,9,20,null,null,15,7]
Output: true



Example 3:

              p              q  
             [1]            [1]
           /                    \
        [2]                     [2]

Input: p = [1,2], q = [1,null,2]
Output: false



Example 4:

              p              q  
             [1]            [1]
           /     \        /     \
        [2]      [1]    [1]     [2]

Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""


class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



    #      p                     q
    #     [3]                   [3]
    #   /     \               /     \
    # [9]      [20]         [9]      [20]
    #         /    \                 /    \
    #      [15]    [7]             [15]    [7]

li1 = [3,9,20,None,None,15,7]
li2 = [3,9,20,None,None,15,7]
output = True

# p Tree
p = Tree(3)
p.left = Tree(9)
p.right = Tree(20)
p.right.left = Tree(15)
p.right.right = Tree(7)

# q Tree
q = Tree(3)
q.left = Tree(9)
q.right = Tree(20)
q.right.left = Tree(15)
q.right.right = Tree(7)

s = Solution()

res = s.isSameTree(p, q)

print(res)
print(output)