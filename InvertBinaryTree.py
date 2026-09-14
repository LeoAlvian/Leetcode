"""
226. Invert Binary Tree

Solved
Easy
Topics
premium lock icon
Companies

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
            [4]                          [4]
         /       \                   /         \  
       [2]       [7]               [7]         [2]
     /     \   /     \           /     \     /     \ 
   [1]    [3] [6]    [9]       [9]    [6]  [3]     [1]

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]



Example 2:


Input: root = [2,1,3]
Output: [2,3,1]




Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Node Class

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

class Solution:
    # Using DFS to solve this problem with time: O(n) and space: O(n)
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # Using Iterative solution
    def invertTreeIterative(self, root):
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    # Printing the node Using BFS
    def print(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            # getting the size of one level
            level_size = len(queue)
            cur_level = []

            # loop through all node in one level
            for i in range(level_size):
                # pop the node from the left
                node = queue.popleft()
                cur_level.append(node.val)
                # if there is node in the left, append it to the queue
                if node.left:
                    queue.append(node.left)
                # if there is node in the right, append it to the queue
                if node.right:
                    queue.append(node.right)
            # add the current level array to the res array
            res += cur_level
            # if you want to add array per level and not join all the array in the res you can use this code below instead
            # res.append(cur_level)

        return res



#             [4]                          [4]
#          /       \                   /         \  
#        [2]       [7]               [7]         [2]
#      /     \   /     \           /     \     /     \ 
#    [1]    [3] [6]    [9]       [9]    [6]  [3]     [1]

li = [4,2,7,1,3,6,9]
output = [4,7,2,9,6,3,1]

s = Solution()

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

newRoot = s.invertTree(root)

res = s.print(newRoot)

print(res)
print(output)