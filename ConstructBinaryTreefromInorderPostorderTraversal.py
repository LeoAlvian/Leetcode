"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Solved
Medium
Topics
premium lock icon
Companies

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

                [3]
              /    \
            [9]     [20]
                   /   \    
                 [15]    [7] 

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]



Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # Time complexity of O(n2) with DFS
    def buildTreeN2(self, inorder, postorder):
        if not inorder:
            return None
        
        root = TreeNode(postorder.pop())

        idx = inorder.index(root.val)
        root.right = self.buildTreeN2(inorder[idx + 1:], postorder)
        root.left = self.buildTreeN2(inorder[:idx], postorder)

        return root
    

    # Time complexity of O(n) with DFS but we gonna add a hash map to make the index
    # calling to be a constant time
    def buildTreeN(self, inorder, postorder):
        mapInorderIdx = { v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            
            root = TreeNode(postorder.pop())

            idx = mapInorderIdx[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)

            return root
        
        return helper(0, len(inorder) - 1)
    

    # BFS lever order traversal
    def printTree(self, root):
        q = deque([root] if root else None)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                res.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res





    #      [3]
    #     /   \
    #  [9]     [20]
    #         /   \    
    #       [15]   [7] 

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
postorder2 = [9,15,7,20,3]
output = [3,9,20,None,None,15,7]

s = Solution()
root = s.buildTreeN2(inorder, postorder)
root2 = s.buildTreeN(inorder, postorder2)
res = s.printTree(root)
res2 = s.printTree(root2)

print(res, "This is O(n2) time")
print(res2, "This is O(n) time")
print(output)