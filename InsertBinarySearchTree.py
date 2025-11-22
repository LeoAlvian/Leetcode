"""
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:



Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]



Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# RECURSIVE FUNCTION
class BST:
    def insertBinarySearchTree(self, root, val):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertBinarySearchTree(root.right, val)
        else:
            root.left = self.insertBinarySearchTree(root.left, val)
        
        return root
    

# TO print the tree into a list we need to traverse it and because the output are 
# design like that so we use preorderTraversal
def preorderTraversal(root):
    stack, res = [], [root.val]
    cur = root

    while cur or stack:
        if cur:
            stack.append(cur.right)
            if cur.left:
                res.append(cur.left.val)
            if cur.right:
                res.append(cur.right.val)
            cur = cur.left
        else:
            cur = stack.pop()
    
    return res


list = [4,2,7,1,3]
val = 5
output = [4,2,7,1,3,5]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

b = BST()
b.insertBinarySearchTree(root, val)
res = preorderTraversal(root)

print(res)
print(output)