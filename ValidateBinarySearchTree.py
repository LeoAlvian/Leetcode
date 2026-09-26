"""
98. Validate Binary Search Tree

Solved
Medium
Topics
premium lock icon
Companies

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

                 [2]
               /     \
             [1]      [3]

Input: root = [2,1,3]
Output: true



Example 2:

                  (-inf, inf)
                      [5]
                    /     \
   (-inf < 1 < 5) [1]      [7]  (5 < 7 < inf)
                          /    \
          x(5 < 4 < 7)  [4]    [8] (7 < 8 < inf)

Input: root = [5,1,7,null,null,4,8]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""



class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

class Solution:
    def isValidBST(self, root):

        # DFS (Depth First Search)
        def valid(node, left, right):
            # Base case
            if not node:
                return True
            # Checking the Boundaries
            if not (left < node.val < right):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float('-inf'), float('inf'))

    def isValidBSTBFS(self, root):
        if not root: 
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True


    #       [5]
    #     /     \
    #   [1]      [7]
    #           /    \
    #         [4]    [8]

li = [5,1,7,None,None,4,8]
output = False

root = Tree(5)
root.left = Tree(1)
root.right = Tree(7)
root.right.left = Tree(4)
root.right.right = Tree(8)

s = Solution()

res = s.isValidBST(root)
res2 = s.isValidBSTBFS(root)

print(res)
print(res2)
print(output)