"""
74. Search a 2D Matrix

Solved
Medium
Topics
premium lock icon
Companies

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

    [ 1, 3, 5, 7]
    [10,11,16,20]
    [23,30,34,60]

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true



Example 2:

    [ 1, 3, 5, 7]
    [10,11,16,20]
    [23,30,34,60]

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


# Using two pass binary search with time: O(log(m * n)) and space: O(1)

def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        m = (top + bot) // 2
        if target > matrix[m][-1]:
            top = m + 1
        elif target < matrix[m][0]:
            bot = m - 1
        else:
            break
    
    if not (top <= bot):
        return False

    mid = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        if target > matrix[mid][m]:
            l = m + 1
        elif target < matrix[mid][m]:
            r = m - 1
        else:
            return True

    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
output = True

res = searchMatrix(matrix, target)

print(res)
print(output)