"""
1267. Count Servers that Communicate

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:


Input: grid = [[1,0],
               [0,1]]
Output: 0
Explanation: No servers can communicate with others.




Example 2:

Input: grid = [[1,0],
               [1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.




Example 3:

Input: grid = [[1,1,0,0],
               [0,0,1,0],
               [0,0,1,0],
               [0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""




def countServers(grid):
    rows, cols = len(grid), len(grid[0])
    row_c = [0] * rows
    col_c = [0] * cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                row_c[r] += 1
                col_c[c] += 1
    
    res = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] and max(row_c[r], col_c[c]) > 1:
                res += 1
    
    return res



# We gonna have row count as row_c and column count as col_c and count every server on that 
# specific location grid[r][c], then we gonna loop through the grid again and see if 
# grid[r][c] > 0 and row_c > 1 or col_c > 1 if yes we gonna increase the result and then 
# return it

# row_c = [1,1,2,1]   col_c
# grid = [[1,1,0,0],   [2]
#         [0,0,1,0],   [1]
#         [0,0,1,0],   [1]
#         [0,0,0,1]]   [1]

grid = [[1,1,0,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,1]]
output = 4

res = countServers(grid)

print(res)
print(output)