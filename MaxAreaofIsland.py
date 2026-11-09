"""
695. Max Area of Island

Solved
Medium
Topics
premium lock icon
Companies

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

    [0,0,1,0,0,0,0,1,0,0,0,0,0]
    [0,0,0,0,0,0,0,1,1,1,0,0,0]
    [0,1,1,0,1,0,0,0,0,0,0,0,0]
    [0,1,0,0,1,1,0,0,1,0,1,0,0]
    [0,1,0,0,1,1,0,0,1,1,1,0,0]
    [0,0,0,0,0,0,0,0,0,0,1,0,0]
    [0,0,0,0,0,0,0,1,1,1,0,0,0]
    [0,0,0,0,0,0,0,1,1,0,0,0,0]

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.



Example 2:

    [0,1,1,0,1]
    [1,0,1,0,1]
    [0,1,1,0,1]
    [0,1,0,0,1]

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6




Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""


# Use DFS to solve this problem with time: O(m * n) and space: O(m * n)

def maxAreaOfIslandDFS(grid):
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    maxArea = 0
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
            return 0

        visited.add((r, c))
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visited:
                maxArea = max(maxArea, dfs(r, c))

    return maxArea




# Solving using BFS with fastest time on leetcode but time complexity is O(m * n) and space: O(m * n) which is the same with DFS

from collections import deque

def maxAreaOfIslandBFS(grid):
    n = len(grid)
    m = len(grid[0])
    queue = deque([])
    # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(i: int, j: int) -> int:
        area = 0
        queue.append((i, j))
        grid[i][j] = 0
        while queue:
            i, j = queue.popleft()
            area += 1

            if i > 0 and grid[i - 1][j]:
                grid[i - 1][j] = 0
                queue.append((i - 1, j))

            if i + 1 < n and grid[i + 1][j]:
                grid[i + 1][j] = 0
                queue.append((i + 1, j))

            if j > 0 and grid[i][j - 1]:
                grid[i][j - 1] = 0
                queue.append((i, j - 1))

            if j + 1 < m and grid[i][j + 1]:
                grid[i][j + 1] = 0
                queue.append((i, j + 1))
        return area
    
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                res = max(res, bfs(i, j))
    return res

    

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
output = 6

res = maxAreaOfIslandDFS(grid)
res2 = maxAreaOfIslandBFS(grid)

print(res)
print(res2)
print(output)