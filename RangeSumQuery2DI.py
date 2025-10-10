"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.

We modify and adding 1 more ROWS and 1 more COLS to the top and left and filled it with 0 so it's gonna be easier to count the matrix
We gonna add each element in the matrix for every ROWS

matrix =
[3, 0, 1, 4, 2], 
[5, 6, 3, 2, 1], 
[1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], 
[1, 0, 3, 0, 5]

self.sumMat =           sumMat (sum per row)        sumMat(sum col and row)
[0, 0, 0, 0, 0, 0],     [0, 0,  0,  0,  0,  0],     [0, 0,   0,  0,  0,  0],
[0, 3, 0, 1, 4, 2],     [0, 3,  3,  4,  8, 10],     [0, 3,   3,  4,  8, 10],
[0, 5, 6, 3, 2, 1], ==> [0, 5, 11, 14, 16, 17], ==> [0, 8,  14, 18, 24, 27],
[0, 1, 2, 0, 1, 5],     [0, 1,  3,  3,  4,  9],     [0, 9,  17, 21, 28, 36],
[0, 4, 1, 0, 1, 7],     [0, 4,  5,  5,  6, 13],     [0, 13, 22, 26, 34, 49],
[0, 1, 0, 3, 0, 5]      [0, 1,  1,  4,  4,  9]      [0, 14, 23, 30, 38, 58]
"""


class SumMatrix:

    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            # prefix 0 so we keep reset the sum for every row
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                # Then we add each prefix row with the sum of the previx above it for
                # the ractangle sum
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, r1, c1, r2, c2):
        # To get the sum of the given ractangle we need to subtract bottom-right 
        # value with (above + left) then adding top-left value
        bottomRight = self.sumMat[r2 + 1][c2 + 1]
        above = self.sumMat[r1][c2 + 1]
        left = self.sumMat[r2 + 1][c1]
        topLeft = self.sumMat[r1][c1]
        return bottomRight - above - left + topLeft



com = ["sumRegion", "sumRegion", "sumRegion"]
matrix = [[3, 0, 1, 4, 2], 
          [5, 6, 3, 2, 1], 
          [1, 2, 0, 1, 5], 
          [4, 1, 0, 1, 7], 
          [1, 0, 3, 0, 5]]
argu = [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
output = [8, 11, 12]

res = []
sm = SumMatrix(matrix)
for i in range(len(com)):
    res.append(getattr(sm, com[i])(*argu[i]))
print(res)
print(output)
print('result == output:', res == output)