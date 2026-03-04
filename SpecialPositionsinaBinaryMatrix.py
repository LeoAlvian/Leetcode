"""
1582. Special Positions in a Binary Matrix

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.



Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
"""


def numSpecial(mat):
    res = 0
    ROWS, COLS = len(mat), len(mat[0])

    for row in range(ROWS):
        for col in range(COLS):
            if mat[row][col] == 0:
                continue
            
            special = True
            for r in range(ROWS):
                if r != row and mat[r][col] == 1:
                    special = False
                    break

            for c in range(COLS):
                if c != col and mat[row][c] == 1:
                    special = False
                    break
            
            if special:
                res += 1
    
    return res



def numSpecialII(mat):
    special = 0

    for row in mat:
        # first iteration
        # row = [1, 0, 0]
        # then check if sum of row is 1
        if sum(row) == 1:
            # get column index of value 1 in a row, in this example column index is 0
            # col_idx_one = 0
            col_idx_one = row.index(1)
            # checking in a column of col_idx_one if it's equal to 1, if it is then 
            # increment special by 1
            special += sum(row[col_idx_one] for row in mat) == 1
    
    return special




mat = [[1,0,0],[0,1,0],[0,0,1]]
output = 3

print(numSpecial(mat))
print(numSpecialII(mat))
print(output)