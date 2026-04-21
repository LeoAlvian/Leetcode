"""
99. Recover Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:

          [1]       [3]
         /          /
       [3]    ->   [1]
         \          \
         [2]        [2]  
    
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.



Example 2:

         [3]              [2]
        /   \            /   \
      [1]   [4]   ->   [1]   [4]
            /                /
         [2]              [3]

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""


from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Using stack with time: O(n) and space: O(n)
    def recoverTree(self, root):
        stack = []
        node1 = node2 = prev = None
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if prev and prev.val > cur.val:
                node2 = cur
                if not node1:
                    node1 = prev
                else:
                    break

            prev = cur
            cur = cur.right
        
        node1.val, node2.val = node2.val, node1.val
    

    # Using Morris traversal, Not using stack so time: O(n) but space: O(1)
    def recoverTreeII(self, root):
        stack = []
        node1 = node2 = prev = None
        curr = root

        while stack or curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    node2 = curr
                    if not node1:
                        node1 = prev
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and prev.val > curr.val:
                        node2 = curr
                        if not node1:
                            node1 = prev
                    prev = curr
                    curr = curr.right
        
        node1.val, node2.val = node2.val, node1.val


    def printLevel(self, root):
        q = deque([root] if root else None)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                res.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res




#          [3]              [2]
#         /   \            /   \
#       [1]   [4]   ->   [1]   [4]
#             /                /
#          [2]              [3]
         
arr = [3,1,4,None,None,2]
output = [2,1,4,None,None,3]

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

s = Solution()
s.recoverTreeII(root)
res = s.printLevel(root)

print(res)
print(output)