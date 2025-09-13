"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
(clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D 
matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
out = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


def rotate(matrix):
    #left and right pointer
    left, right = 0, len(matrix) - 1

    while left < right:
        #top and bottom pointer set to be equal to left and right
        #because they have the same value and change in the same pace
        top, bottom = left, right
        #create for loop so the loop gonna get smaller for inner bound
        #rectangle
        #also we looping on the counter clockwise so we can save space
        #we just need one v
        for i in range(right - left):
            #store top left to the temp topLeft variable
            topLeft = matrix[top][left + i]
            #change top left to bottom left
            matrix[top][left + i] = matrix[bottom - i][left]
            #change bottom left to bottom right
            matrix[bottom - i][left] = matrix[bottom][right - i]
            #change bottom rigth to top right
            matrix[bottom][right - i] = matrix[top + i][right]
            #change top right to top left which is in the topLeft temp variable
            matrix[top + i][right] = topLeft

        #increase the left and right for the inner ractangle
        left += 1
        right -= 1


print(matrix)
rotate(matrix)
print(matrix)
print(out == matrix)
