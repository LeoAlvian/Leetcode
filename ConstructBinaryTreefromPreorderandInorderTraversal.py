"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Solved
Medium
Topics
premium lock icon
Companies

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

                [3]
              /    \
            [9]     [20]
                   /   \    
                 [15]    [7]

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]



Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""



class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

class Solution:
    # Using DFS with time: O(n2) and space: O(n)
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = Tree(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root



    # Hash Map + Depth First Search with time: O(n) and space: O(n)
    
    def buildTreeHash(self, preorder, inorder):
        idx_map = { val: i for i, val in enumerate(inorder)}
        self.index = 0

        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = Tree(root_val)

            mid = idx_map[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)


    # Print the tree in level order or BFS
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


            #    [3]
            #   /    \
            # [9]     [20]
            #        /   \    
            #      [15]    [7]

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
output = [3,9,20,None,None,15,7]

s = Solution()

root = s.buildTree(preorder, inorder)
root2 = s.buildTreeHash(preorder, inorder)

res = s.printTree(root)
res2 = s.printTree(root2)

print(res, 'O(n2) Time')
print(res2, 'O(n) Time')
print(output)