"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]



Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.



Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]

Explanation: The tree does not contain a node with value = 0.



Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
"""


# root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
#
#            [5]
#          /     \
#       [3]     [6]
#       /   \       \
#     [2]   [4]     [7]
#
#            [5]
#          /     \
#        [4]     [6]
#       /           \
#     [2]           [7]
# 
# We check if root is None
# if key < root.val: using recursive to deleteBST to the left 
# elif key > root.val: using recursive to deleteBST to the right
# else: 
# if root.left is None: return root.right
# elif root.right is None: return root.left
# assign cur = root.right
# traverse through the left side until reach the end of the tree
# while cur.left: cur = cur.left
# assign root.val = cur.val
# call recursive function to delete the cur node that we move to the root
# root.right = deleteBST(root.right, root.val)
# return root

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def deleteBST(self, root, key):
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteBST(root.right, key)
        elif key < root.val:
            root.left = self.deleteBST(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteBST(root.right, root.val)
        return root

    # TO print the tree into a list we need to traverse it and because the output are 
    # design like that so we use preorderTraversal
    def preorderTraversal(self, root):
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


list = [5,3,6,2,4,None,7]
key = 3
output = [5,4,6,2,None,None,7]

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)
s = Solution()
s.deleteBST(root, key)
res = s.preorderTraversal(root)
print(res)
print(output)