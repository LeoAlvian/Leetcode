"""
934. Shortest Bridge

Solved
Medium
Topics
premium lock icon
Companies

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1



Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2



Example 3:

      [1,1,1,1,1]
      [1,0,0,0,1]
      [1,0,1,0,1]
      [1,0,0,0,1]
      [1,1,1,1,1]

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1



Example 4:

      [0,1,0,0,0]
      [0,1,0,0,0]
      [1,1,0,0,1]
      [0,0,0,0,1]
      [0,0,0,0,1]

Input: grid = [[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
Output: 2
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""


from collections import deque


def shortestBridge(grid):
    N = len(grid)
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1),]

    def isvalid(r, c):
        return r < 0 or c < 0 or r >= N or c >= N
    
    visit = set()
    def dfs(r, c):
        if isvalid(r,c) or not grid[r][c] or (r,c) in visit:
            return
        visit.add((r, c))
        for dr, dc in direct:
            dfs(r + dr, c + dc)
    
    def bfs():
        res = 0
        q = deque(visit)

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    curR, curC = r + dr, c + dc
                    if isvalid(curR, curC) or (curR, curC) in visit:
                        continue
                    if grid[curR][curC]:
                        return res
                    q.append((curR, curC))
                    visit.add((curR, curC))
            res += 1


    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                dfs(r, c)
                return bfs()


    # [0,1,0,0,0]
    # [0,1,0,0,0]
    # [1,1,0,0,1]
    # [0,0,0,0,1]
    # [0,0,0,0,1]

# Scan through the grid vertically and horizontally using DFS and add all the is 1 to the 
# visit hash set, then scan again through the grid using BFS to count how many 0's we need
# to flip to make a bridge

grid = [[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
output = 2

res = shortestBridge(grid)

print(res)
print(output)