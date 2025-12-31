"""
Docstring for MinimumPathSum

64. Minimum Path Sum

Solved
Medium
Topics
premium lock icon
Companies

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.



Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [float('inf')] * (cols + 1)
    dp[cols - 1] = 0

    for r in reversed(range(rows)):
        for c in reversed(range(cols)):
            dp[c] = grid[r][c] + min(dp[c], dp[c + 1])
    
    return dp[0]


grid = [[1,3,1],[1,5,1],[4,2,1]]
output = 7
mp = minPathSum(grid)
print(mp)
print(output)
