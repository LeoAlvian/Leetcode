"""
994. Rotting Oranges

Solved
Medium
Topics
premium lock icon
Companies

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:

    minute 0    minute 1    minute 2    minute 3    minute 4

    [2,1,1]     [2,2,1]     [2,2,2]     [2,2,2]     [2,2,2]
    [1,1,0]     [2,1,0]     [2,2,0]     [2,2,0]     [2,2,0]
    [0,1,1]     [0,1,1]     [0,1,1]     [0,2,1]     [0,2,2]

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4



Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.



Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


# Solve using BFS Recursively with time: O(m * n) and space: O(m * n)

from collections import deque

def orangesRotting(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    visit = set()
    time, fresh = 0, 0

    def bfs(r, c):
        nonlocal fresh
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
            return
        visit.add((r, c))
        fresh -= 1
        q.append([r, c])

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append([r, c])
                visit.add((r, c))

    while q and fresh:
        for i in range(len(q)):
            r, c = q.popleft()
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)
        time += 1

    return time if not fresh else -1




# Solve using BFS Recursively with time: O(m * n) and space: O(1) extra space because we modify the grid in place

def orangesRottingII(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    time, fresh = 0, 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append([r, c])

    if not fresh:
        return 0

    while q and fresh:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    q.append([nr, nc])
                    fresh -= 1
                    grid[nr][nc] = 2
        time += 1

    return time if not fresh else -1




grid = [[2,1,1],[1,1,0],[0,1,1]]
output = 4 

res = orangesRotting(grid)
res2 = orangesRottingII(grid)

print(res)
print(res2)
print(output)