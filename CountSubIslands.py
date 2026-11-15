"""
1905. Count Sub Islands

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:
    grid 1          grid 2       
    [1,1,1,0,0]     [1,1,1,0,0]    
    [0,1,1,1,1]     [0,0,1,1,1]     
    [0,0,0,0,0]     [0,1,0,0,0]     
    [1,0,0,0,0]     [1,0,1,1,0]           
    [1,1,0,1,1]     [0,1,0,1,0]


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.



Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""



def countSubIslands(grid1, grid2):
    ROWS, COLS = len(grid1), len(grid1[0])
    visit = set()
    count = 0

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0 or (r, c) in visit:
            return True

        visit.add((r, c))
        res = True
        if grid1[r][c] == 0:
            res = False

        res = dfs(r + 1, c) and res
        res = dfs(r - 1, c) and res
        res = dfs(r, c + 1) and res
        res = dfs(r, c - 1) and res
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                count += 1

    return count




def countSubIslandsII(grid1, grid2):
    # find island in grid2 
    # check if the same island exists in grid1 
    ROWS, COLS = len(grid2), len(grid2[0])

    def dfs(r, c): 
        if grid1[r][c] != 1: 
            # this island is not be considered in count 
            # skip the dfs 
            return False 

        grid2[r][c] = -1 
        grid1[r][c] = -1 

        temp1 = temp2 = temp3 = temp4 = True 

        if r > 0 and grid2[r - 1][c] == 1: 
            temp1 = dfs(r - 1, c)
        if c > 0 and grid2[r][c - 1] == 1: 
            temp2 = dfs(r, c - 1)
        if r + 1 < ROWS and grid2[r + 1][c] == 1:
            temp3 = dfs(r + 1, c)
        if c + 1 < COLS and grid2[r][c + 1] == 1: 
            temp4 = dfs(r,c + 1)

        return temp1 and temp2 and temp3 and temp4 
    
    count = 0 

    for r in range(ROWS):
        for c in range(COLS):
            if grid2[r][c] == 1 and dfs(r, c):  
                    count += 1 

    return count 



grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
output = 3

res = countSubIslands(grid1, grid2)
res2 = countSubIslandsII(grid1, grid2)

print(res)
print(res2)
print(output)