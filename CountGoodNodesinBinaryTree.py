"""
1448. Count Good Nodes in Binary Tree

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

                +[3]
               /     \
             [1]     +[4]
            /        /    \
        +[3]       [1]  +[5]
                       
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.




Example 2:

                +[3]
               /     
            +[3]      
            /   \
         +[4]    [2]

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.




Example 3:

               +[1]
               /   \  
            +[2]   [-1]  
            /   \
         +[3]   +[4]

Input: root = [1,2,-1,3,4]
Output: 4




Example 4:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""



class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

class Solution:
    # Solving it using DFS preorder traversal with time: O(n) and space: O(n) for call stack
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)


    def goodNodesII(self, root):
        def helper(root, maxVal):
            if root is None:
                return 0

            if root.val < maxVal:
                return helper(root.left, maxVal) + helper(root.right, maxVal)
            else:
                # case: root.val >= upper_bound
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
        return helper(root, root.val)


    # Using BFS with time: O(n) and space: O(n)

    def goodNodesBFS(self, root):
        res = 0
        q = deque()

        q.append((root, float('-inf')))

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1

            if node.left:
                q.append((node.left, max(maxVal, node.val)))

            if node.right:
                q.append((node.right, max(maxVal, node.val)))

        return res


        #         +[3]
        #        /     \
        #      [1]     +[4]
        #     /        /    \
        # +[3]       [1]  +[5]
                       
li = [3,1,4,3,None,1,5]
output = 4

root = Tree(3)
root.left = Tree(1)
root.right = Tree(4)
root.left.left = Tree(3)
root.right.left = Tree(1)
root.right.right = Tree(5)

s = Solution()

res = s.goodNodes(root)
res2 = s.goodNodesII(root)
res3 = s.goodNodesBFS(root)

print(res)
print(res2)
print(res3)
print(output)