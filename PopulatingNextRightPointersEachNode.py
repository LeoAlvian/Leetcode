"""
116. Populating Next Right Pointers in Each Node

Solved
Medium
Topics
premium lock icon
Companies

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.



Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""


from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        
        return root

    def printBST(self, root):
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                res.append(node.val)
                if not node.next:
                    res.append('#')
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return res




#                 [1]
#               /     \
#             [2]      [3]
#            /   \    /    \
#         [4]    [5] [6]   [7]
arr = [1,2,3,4,5,6,7]
output = [1,'#',2,3,'#',4,5,6,7,'#']


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()

newRoot = s.connect(root)
res = s.printBST(newRoot)

print(res)
print(output)