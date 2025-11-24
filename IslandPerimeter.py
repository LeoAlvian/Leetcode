"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.



Example 2:

Input: grid = [[1]]
Output: 4



Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""


# Using Depth First Search Algorithm to solve the problem
def islandParimeterDFS(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    def dfs(i, j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        visited.add((i, j))
        parim = dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
        return parim 

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                return dfs(r, c)
    
    return 0


grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]
output = 16

res = islandParimeterDFS(grid)
print(res)

print(output)
