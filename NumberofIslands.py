"""
200. Number of Islands

Solved
Medium
Topics
premium lock icon
Companies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1



Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Example 3:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


# Using DFS with time: O(m * n) and space: O(m * n)

def numIslandsDFS(grid):
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    island = 0
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0' or (r, c) in visited:
            return

        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                island += 1

    return island





# Using BFS with time: O(m * n) and space: O(m * n)
from collections import deque

def numIslandsBFS(grid):
    if not grid:
        return 0

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    island = 0
    visited = set()
    ROWS, COLS = len(grid), len(grid[0])

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                newR, newC = row + dr, col + dc
                if newR in range(ROWS) and newC in range(COLS) and grid[newR][newC] == '1' and (newR, newC) not in visited:
                    q.append((newR, newC))
                    visited.add((newR, newC))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                island += 1

    return island

    




grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
output = 4

res = numIslandsDFS(grid)
res2 = numIslandsBFS(grid)

print(res)
print(res2)
print(output)