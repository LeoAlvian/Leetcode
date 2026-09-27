"""
230. Kth Smallest Element in a BST

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:

                [3]
               /   \
             [1]   [4]
                \    
               [2] 
              
Input: root = [3,1,4,null,2], k = 1
Output: 1




Example 2:

                 [5]
               /     \
             [3]      [6]
            /   \    
         [2]    [4] 
        /      
      [1]     

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""


class Tree:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None



class Solution:
    # Solve Using Inorder DFS Recursive, time: O(n) and space: O(n) for calling stack function
    def kthSmallest(self, root):
        arr = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]



    #              [5]
    #            /     \
    #          [3]      [6]
    #         /   \    
    #      [2]    [4] 
    #     /      
    #   [1]     

li = [5,3,6,2,4,None,None,1]
k = 3
output = 3

root = Tree(5)
root.left = Tree(3)
root.right = Tree(6)
root.left.left = Tree(2)
root.left.right = Tree(4)
root.left.left.left = Tree(1)

s = Solution()

res = s.kthSmallest(root)

print(res)
print(output)