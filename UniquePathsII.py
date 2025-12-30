"""
Docstring for UniquePathsII

63. Unique Paths II

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right



Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


# We solve this using Dynamic Programming and using list of size col to store the value,
# First we set the destination (Bottom-Left) to be 1 and calculate the path from there by 
# adding the cell below and to the right of it
#
# grid = [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 1, 0]
#        ]
#
# iteration 1
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
# 
#       2 [0, 1, 0]    -> x at grid[2][2]
#        ]       x
#
# dp =    [0, 0, 1]    -> set dp[c] -> dp[2] = 1
#
# iteration 2 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
# 
#       2 [0, 1, 0]    -> x at grid[2][1]
#        ]    x
#
# dp =    [0, 0, 1]    -> because there is obstacle so we set dp[1] = 0
# 
# iteration 3 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
# 
#       2 [0, 1, 0]    -> x at grid[2][0] 
#        ] x
#
# dp =    [0, 0, 1]    -> set dp[0] = dp[0] + dp[0 + 1] = 0 + 0 = 0
# 
# iteration 4 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
#                x
#       2 [0, 1, 0]    -> x at grid[1][2] 
#        ] 
#
# dp =    [0, 0, 1]    -> because dp[2 + 1](out of range) so we didn't do anything 
# 
# iteration 5 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
#             x
#       2 [0, 1, 0]    -> x at grid[1][1] 
#        ] 
#
# dp =    [0, 1, 1]    -> set dp[1] = dp[1] + dp[1 + 1] = 0 + 1 = 1 
# 
# iteration 6 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#       
#       1 [0, 0, 0],   -> x is the pointer
#          x
#       2 [0, 1, 0]    -> x at grid[1][0] 
#        ] 
#
# dp =    [1, 1, 1]    -> set dp[0] = dp[0] + dp[0 + 1] = 0 + 1 = 1 
# 
# iteration 7 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#                x
#       1 [0, 0, 0],   -> x is the pointer
#          
#       2 [0, 1, 0]    -> x at grid[0][2] 
#        ] 
#
# dp =    [1, 1, 1]    -> set dp[2] = dp[2] + dp[2 + 1] = 1 + 0 = 1 (out of range)
# 
# iteration 8 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#             x
#       1 [0, 0, 0],   -> x is the pointer
#          
#       2 [0, 1, 0]    -> x at grid[0][1] 
#        ] 
#
# dp =    [1, 2, 1]    -> set dp[1] = dp[1] + dp[1 + 1] = 1 + 1 = 2
# 
# iteration 9 
# grid = [ 0  1  2
#       0 [0, 0, 0],
#          x
#       1 [0, 0, 0],   -> x is the pointer
#          
#       2 [0, 1, 0]    -> x at grid[0][0] 
#        ] 
#
# dp =    [3, 2, 1]    -> set dp[0] = dp[0] + dp[1 + 1] = 1 + 2 = 3
# 
# exit loop, then we return dp[0] = 3

def uniquePathII(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [0] * cols 
    dp[cols - 1] = 1

    # Both of this reverse loop are the same
    for r in reversed(range(rows)):
        for c in range(cols - 1, -1, -1):
            if grid[r][c]:
                dp[c] = 0
            elif c + 1 < cols:
                dp[c] = dp[c] + dp[c + 1]
    
    return dp[0]


grid = [
        [0,0,0],
        [0,0,0],
        [0,1,0]
        ]
output = 3
up = uniquePathII(grid)
print(up)
print(output)