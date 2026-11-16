"""
417. Pacific Atlantic Water Flow

Solved
Medium
Topics
premium lock icon
Companies

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:

        Pacific
  Pa  [1,2,2,3,5]  At
  ci  [3,2,3,4,4]  la
  f   [2,4,5,3,1]  n
  i   [6,7,1,4,5]  ti
  c   [5,1,1,2,4]  c
        Atlantic
  
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.




Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""



def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    res = []

    def dfs(r, c, visit, prevH):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevH or (r, c) in visit:
            return

        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    # Go from first column and last column backward
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    # Go from first row and last row backward
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    # Go through every grid and if the current coordinate is in pacivic and atlancit set then the current coordinate can reach both
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res




# Second function using dynamic programming which is faster on leetcode

def pacificAtlanticDP(heights):
    ROWS, COLS = len(heights), len(heights[0])
    dp = [[0] * COLS for _ in range(ROWS)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []

    def dfs(r, c, val):
        if dp[r][c] == val:
            return
        if dp[r][c] == -val:
            res.append([r, c])
        dp[r][c] = val
        stack = [(r, c)]
        while stack:
            sr, sc = stack.pop()
            for dr, dc in dirs:
                r, c = sr + dr, sc + dc
                if (0 <= r < ROWS and 0 <= c < COLS
                        and dp[r][c] != val
                        and heights[sr][sc] <= heights[r][c]):
                    if dp[r][c] == -val:
                        res.append([r, c])
                    dp[r][c] = val
                    stack.append((r, c))

    # Pacific: top row + left column — must fully finish first
    for c in range(COLS):
        dfs(0, c, 1)
    for r in range(ROWS):
        dfs(r, 0, 1)

    # Atlantic: bottom row + right column
    for c in range(COLS):
        dfs(ROWS - 1, c, -1)
    for r in range(ROWS):
        dfs(r, COLS - 1, -1)

    return res




heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

res = pacificAtlantic(heights)
res2 = pacificAtlanticDP(heights)

print(res)
print(res2)
print(output)


# Printing the grid with the coordinate

# for r in range(len(heights)):
#     print(heights[r])

# print('----------------------------------')

# for r, c in res:
#     heights[r][c] = 0

# for r in range(len(heights)):
#     print(heights[r])