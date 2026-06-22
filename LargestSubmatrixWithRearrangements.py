"""
1727. Largest Submatrix With Rearrangements

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:

    [0,0,1]      [0,1,0] 
    [1,1,1]  ->  [1,1,1]
    [1,0,1]      [1,1,0]

Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.




Example 2:

    [1,0,1,0,1]     [1,1,1,0,0]

Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.




Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
"""


def largestSubmatrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    res = 0
    prev_heights = [0] * COLS

    for r in range(ROWS):
        heights = matrix[r][::]
        for c in range(COLS):
            if heights[c] > 0:
                heights[c] += prev_heights[c]
        sorted_height = sorted(heights, reverse=True)

        for i in range(len(sorted_height)):
            res = max(res, (i + 1) * sorted_height[i])
        
        prev_heights = heights


    return res


matrix = [[0,0,1],[1,1,1],[1,0,1]]
output = 4

res = largestSubmatrix(matrix)

print(res)
print(output)