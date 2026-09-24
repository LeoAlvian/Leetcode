"""
427. Construct Quad Tree

Solved
Medium
Topics
premium lock icon
Companies

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:

    [0,1]                        [isLeaf : 0]
    [1,0]                        [val : 1   ] 
                                      |
            -----------------------------------------------------
            |                |                 |                |
         topLeft          topRight         bottomLeft      bottomRight
            |                |                 |                |
            v                v                 v                v
        [isLeaf : 1]     [isLeaf : 1]      [isLeaf : 1]    [isLeaf : 1]
        [val    : 0]     [val    : 1]      [val    : 1]    [val    : 0]

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.



Example 2:

    [1,1,1,1,|0,0,|0,0]                             [isLeaf : 0]
    [1,1,1,1,|0,0,|0,0]                             [val : 1   ] 
    [        |--------]                                   |
    [1,1,1,1,|1,1,|1,1]      -----------------------------------------------------   
    [1,1,1,1,|1,1,|1,1]      |                |                 |                |
    [-----------------]   topLeft          topRight         bottomLeft      bottomRight
    [1,1,1,1,|0,0,0,0 ]      |                |                 |                |
    [1,1,1,1,|0,0,0,0 ]      v                v                 v                v
    [1,1,1,1,|0,0,0,0 ]  [isLeaf : 1]     [isLeaf : 0]      [isLeaf : 1]    [isLeaf : 1]
    [1,1,1,1,|0,0,0,0 ]  [val    : 1]     [val    : 1]      [val    : 1]    [val    : 0]
                                                |
                      ----------------------------------------------------- 
                      |                |                 |                |
                   topLeft          topRight         bottomLeft      bottomRight
                      |                |                 |                |
                      v                v                 v                v
                [isLeaf : 1]     [isLeaf : 1]      [isLeaf : 1]    [isLeaf : 1]
                [val    : 0]     [val    : 0]      [val    : 1]    [val    : 1]

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6
"""


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    # Solving it using DFS with time: O(n2 logn) and space: O(n)
    def ConstructQuadTree(self,grid):
        def dfs(n, row, col):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[row][col], 1)

            n = n // 2
            topleft = dfs(n, row, col)
            topright = dfs(n, row, col + n)
            bottomleft = dfs(n, row + n, col)
            bottomright = dfs(n, row + n, col + n)

            return Node(0, 0, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)

    # Another way of solving it with the same time complexity

    def ConstructQuadTreeII(self, grid):
        def dfs(n, r, c):
            val = grid[r][c]
            if all(grid[r + i][c + j] == val for i in range(n) for j in range(n)):
                return Node(grid[r][c], 1)
            h = n // 2
            return Node(0, 0, dfs(h, r, c), dfs(h, r, c + h),
                                    dfs(h, r + h, c), dfs(h, r + h, c + h))
        return dfs(len(grid), 0, 0)


    # Printing the tree to an array

    def printTree(self,root):
        res = []
        def dfs(root):
            if not root:
                return

            topleft = dfs(root.topLeft)
            topright = dfs(root.topRight)
            bottomleft = dfs(root.bottomLeft)
            bottomright = dfs(root.bottomRight)

            res.append([root.val, root.isLeaf])
            
            return [root.val, root.isLeaf]
        return (dfs(root), res)

grid = [
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0]
    ]
output = [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]]
s = Solution()
root = s.ConstructQuadTree(grid)
root2 = s.ConstructQuadTreeII(grid)
print(root)
_, res = s.printTree(root)
_, res2 = s.printTree(root2)
print(res)
print(res2)
print(output)