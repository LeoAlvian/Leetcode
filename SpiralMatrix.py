"""
Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = [1,2,3,4,8,12,11,10,9,5,6,7]

def SpiralMatrix(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    # loop through until left < right and top < bottom so we can get the 
    # inner circle as well
    while left < right and top < bottom:
        # loop from left to right and add all top matrix to the result 
        # and then shrink the top pointer
        for i in range(left, right):
            res.append(matrix[left][i])
        top += 1

        # loop from top right to bottom right and add all top matrix to the result 
        # and then shrink the right pointer
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        
        # to exit the loop if the matrix is not square
        if not (left < right and top < bottom):
            break

        # loop from bottom right to bottom left and add all top matrix to the result 
        # and then shrink the bottom pointer
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # loop from bottom left to top left and add all top matrix to the result 
        # and then shrink the left pointer
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    
    return res


result = SpiralMatrix(matrix)
print(result)
print('Is result the same as output:', result == output)