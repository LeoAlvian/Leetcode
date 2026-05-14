"""
221. Maximal Square

Solved
Medium
Topics
premium lock icon
Companies

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:

    ["1","0","1","0","0"]
    ["1","0","1","1","1"]
    ["1","1","1","1","1"]
    ["1","0","0","1","0"]

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4



Example 2:

    ["0","1"]
    ["1","0"]

Input: matrix = [["0","1"],["1","0"]]
Output: 1



Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""



# Top-Down Dynamic Programming using DFS with time: O(m * n) and space: O(m * n)
def maximalSquareII(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    cache = {} # map (r, c) to length of square

    def dfs(r, c):
        if r >= ROWS or c >= COLS:
            return 0
        
        if (r, c) not in cache:
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)
            cache[(r, c)] = 0
            if matrix[r][c] == '1':
                cache[(r, c)] = 1 + min(down, right, diag)

        return cache[(r, c)]
    
    dfs(0, 0)
    return max(cache.values()) ** 2


# Bottom-Up Dynamic Programming with time: O(m * n) and space: O(m * n)
def maximalSquare(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = [[0] * (COLS + 1) for i in range(ROWS + 1)]
    maxSide = 0

    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            if matrix[r][c] == '1':
                dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                maxSide = max(maxSide, dp[r][c])
    
    return maxSide * maxSide



    # ["1","0","1","0","0"]
    # ["1","0","1","1","1"]
    # ["1","1","1","1","1"]
    # ["1","0","0","1","0"]

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
output = 4

res = maximalSquare(matrix)
res2 = maximalSquareII(matrix)

print(res)
print(res2)
print(output)