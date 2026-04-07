"""
590. N-ary Tree Postorder Traversal

Solved
Easy
Topics
premium lock icon
Companies

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:
             [1]
          /   |    \
       [3]   [2]   [4]
      /  \
    [5]  [6]
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]



Example 2:
                   [1]
                / |  |  \
              /   |  |    \
            /    /    \     \
          /     /      \      \
       [2]    [3]      [4]    [5] 
             /  \       |    /    \
           [6]  [7]    [8]  [9]   [10]
                 |      |    |
                [11]   [12] [13]
                 |
                [14]
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class Node:
    def __init__(self, val = 0, children = []):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        res = []
        if not root:
            return []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for child in node.children[::-1]:
                    stack.append((child, False))

        return res



listNode = [1,None,3,2,4,None,5,6]
output = [5,6,3,2,4,1]
#              [1]
#           /   |    \
#        [3]   [2]   [4]
#       /  \
#     [5]  [6]

root = Node(1)
root.children = [3,2,4]
root.children[0] = Node(3)
root.children[1] = Node(2)
root.children[2] = Node(4)
root.children[0].children = [5,6]
root.children[0].children[0] = Node(5)
root.children[0].children[1] = Node(6)

# print(root.children[0].children[0].val)

s = Solution()

res = s.postorder(root)

print(res)
print(output)