"""
235. Lowest Common Ancestor of a Binary Search Tree

Solved
Medium
Topics
premium lock icon
Companies

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

                 [6]
               /     \
           p [2]   q [8]
            /   \    /    \
         [0]    [4] [7]   [9]
               /  \
             [3]  [5]

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.




Example 2:

                 [6]
               /     \
           p [2]      [8]
            /   \    /    \
         [0]  q [4] [7]   [9]
               /  \
             [3]  [5]

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""



class Tree:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur






    #          [6]
    #        /     \
    #    p [2]      [8]
    #     /   \    /    \
    #  [0]  q [4] [7]   [9]
    #        /  \
    #      [3]  [5]

li = [6,2,8,0,4,7,9,None, None,3,5]
p = 2
q = 4
output = 2

root = Tree(6)
root.left = Tree(2)
root.right = Tree(8)
root.left.left = Tree(0)
root.left.right = Tree(4)
root.left.right.left = Tree(3)
root.left.right.right = Tree(5)
root.right.left = Tree(7)
root.right.right = Tree(9)

p = Tree(2)
q = Tree(4)

s = Solution()

res = s.lowestCommonAncestor(root, p, q)

print(res.val)
print(output)