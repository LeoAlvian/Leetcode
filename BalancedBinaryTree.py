"""
110. Balanced Binary Tree

Solved
Easy
Topics
premium lock icon
Companies

Given a binary tree, determine if it is height-balanced.

 

Example 1:

                [3]
              /     \   
            [9]      [20]
                    /   \
                [15]    [7]

Input: root = [3,9,20,null,null,15,7]
Output: true



Example 2:

             [1]
           /     \
        [2]      [2]
      /     \   
    [3]      [3]
   /   \    
 [4]   [4] 

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false



Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""



class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):

        # Helper function to return height, or -1 if unbalanced
        def check_height(node):
            if not node: # so if there is no more node then the height is 0 duh 
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1 # Left subtree is unbalanced, bubble up the failure
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1 # Right subtree is unbalanced, bubble up the failure
            
            # Check if current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return actual height if balanced
            return 1 + max(left_height, right_height)
        
        # If check_height returns anything other than -1, it's balanced
        return check_height(root) != -1 # because all the rest was not balanced




        #     [3]
        #   /     \   
        # [9]      [20]
        #         /   \
        #     [15]    [7]

li = [3,9,20,None,None,15,7]
output = True

root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

s = Solution()

res = s.isBalanced(root)

print(res)
print(output)