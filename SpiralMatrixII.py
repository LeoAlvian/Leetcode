"""
59. Spiral Matrix II

Solved
Medium
Topics
premium lock icon
Companies

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:
       L   R
    T [1,2,3]
      [8,9,4]
    B [7,6,5]

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]



Example 2:
     L           R
    T [1,   2,  3, 4]
      [12, 13, 14, 5]
      [11, 16, 15, 6]
    B [10,  9,  8, 7]

Input: n = 4
Output: [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]


Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""


def generateMatrix(n):
    matrix = [[0] * n for i in range(n)]
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    val = 1

    while top <= bottom:
        # Top Row from left to right
        for r in range(left, right + 1):
            matrix[top][r] = val
            val += 1
        top += 1

        # Right Col from top to bottom
        for c in range(top, bottom + 1):
            matrix[c][right] = val
            val += 1
        right -= 1

        # Bottom Row from right to left (reverse)
        for r in range(right, left - 1, -1):
            matrix[bottom][r] = val
            val += 1
        bottom -= 1

        # Left Col from bottom to top (reverse)
        for c in range(bottom, top - 1, -1):
            matrix[c][left] = val
            val += 1
        left += 1
    
    return matrix
    


n = 4
output = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

res = generateMatrix(n)

print(res)
print(output)