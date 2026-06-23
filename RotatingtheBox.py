"""
1861. Rotating the Box

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:

Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]



Example 2:

Input: boxGrid = [["#",".","*","."],
                  ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]



         
Example 3:

Input: boxGrid = [["#","#","*",".","*","."],
                  ["#","#","#","*",".","."],
                  ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
"""


# Swap in place with time O(m * n) and space O(1)
def rotateTheBox(boxGrid):
    ROWS, COLS = len(boxGrid), len(boxGrid[0])

    # swapping the stones in place
    for r in range(ROWS):
        i = COLS - 1
        for c in reversed(range(COLS)):
            if boxGrid[r][c] == "#":
                boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                i -= 1
            elif boxGrid[r][c] == "*":
                i = c - 1

    # rotating the matrix
    res = []
    for c in range(COLS):
        col = []  # this is a row after rotation
        for r in reversed(range(ROWS)):
            col.append(boxGrid[r][c])
        res.append(col)

    return res



def rotateTheBox(boxGrid):
    ROWS, COLS = len(boxGrid), len(boxGrid[0])
    res = [['.'] * ROWS for i in range(COLS)]

    for r in range(ROWS):
        i = COLS - 1
        for c in reversed(range(COLS)):
            if boxGrid[r][c] == '#':
                res[i][ROWS - r - 1] = '#'
                i -= 1
            elif boxGrid[r][c] == '*':
                res[c][ROWS - r - 1] = '*'
                i = c - 1
    
    return res




boxGrid = [["#","#","*",".","*","."],
           ["#","#","#","*",".","."],
           ["#","#","#",".","#","."]]
output = [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

res = rotateTheBox(boxGrid)

print('     Output            Result')
print('----------------------------------')
for i in range(len(res)):
    print(output[i], '|', res[i])