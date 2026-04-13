"""
Lowest Common Ancestor of a Binary Tree III

Medium
Topics
Company Tags

You are given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."



Example 1:

                  [5]
                /     \
              [3]      [4]
             /   \    
          [2]    [1]            

Input: root = [5,3,4,2,1], p = 1, q = 2
Output: 3



Example 2:

                   [5]
                /      \
             [3]       [4]
            /    \        \
          [2]      [1]      [9]
             \    /   \
            [11] [10] [12]

Input: root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12
Output: 3



Constraints:

2 <= The number of nodes in the tree <= 100,000.
-1,000,000,000 <= Node.val <= 1,000,000,000
All Node.val are unique.
p != q
p and q will both exist in the tree.

"""



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p, q):
        ptr1, ptr2 = p, q
        while ptr1 != ptr2:
            ptr1 = ptr1.parent if ptr1 else q
            ptr2 = ptr2.parent if ptr2 else p
        
        return ptr1



#                   [5]
#                 /      \
#              [3]       [4]
#             /    \        \
#           [2]      [1]      [9]
#              \    /   \
#             [11] [10] [12]

arr = [5,3,4,2,1,None,9,None,11,10,12]
p = 3
q = 12
output = 3

root = TreeNode(5)
root.left = TreeNode(3)
root.left.parent = root
root.right = TreeNode(4)
root.right.parent = root
root.left.left = TreeNode(2)
root.left.left.parent = root.left
root.left.right = TreeNode(1)
root.left.right.parent = root.left
root.right.right = TreeNode(9)
root.right.right.parent = root.right
root.left.right.left = TreeNode(10)
root.left.right.left.parent = root.left.right
root.left.right.right = TreeNode(12)
root.left.right.right.parent = root.left.right
root.left.left.right = TreeNode(11)
root.left.left.right.parent = root.left.left
p = root.left
q = root.left.right.right

s = Solution()

res = s.lowestCommonAncestor(p, q)

print(res.val)
print(output)