"""
1020. Number of Enclaves

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

        [0,0,0,0]
        [1,0,1,0]
        [0,1,1,0]
        [0,0,0,0]
    
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.



Example 2:

        [0,1,1,0]
        [0,0,1,0]
        [0,0,1,0]
        [0,0,0,0]

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""


# Solve using DFS
def numEnclaves(grid):
    rows, cols = len(grid), len(grid[0])
    land, edgeLand = 0, 0
    visit = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c] or (r, c) in visit:
            return 0
        visit.add((r, c))
        res = 1
        for dr, dc in dirs:
            res += dfs(r + dr, c + dc)
        
        return res

    for r in range(rows):
        for c in range(cols):
            land += grid[r][c]
            if (r in [0, rows - 1] or c in [0, cols - 1]) and grid[r][c] and (r, c) not in visit:
                edgeLand += dfs(r, c)

    return land - edgeLand

        # [0,0,0,0]
        # [1,0,1,0]
        # [0,1,1,0]
        # [0,0,0,0]
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
output = 3

res = numEnclaves(grid)

print(res)
print(output)