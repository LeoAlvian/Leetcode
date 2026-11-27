"""
1958. Check if Move is Legal

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:


Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.

 

Example 1:
       0   1   2   3   4   5   6   7
  0  [".",".",".","B",".",".",".","."]
  1  [".",".",".","W",".",".",".","."]
  2  [".",".",".","W",".",".",".","."]
  3  [".",".",".","W",".",".",".","."]
  4  ["W","B","B","X","W","W","W","B"]
  5  [".",".",".","B",".",".",".","."]
  6  [".",".",".","B",".",".",".","."]
  7  [".",".",".","W",".",".",".","."]

Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.



Example 2:
       0   1   2   3   4   5   6   7
  0  [".",".",".",".",".",".",".","."]
  1  [".","B",".",".","W",".",".","."]
  2  [".",".","W",".",".",".",".","."]
  3  [".",".",".","W","B",".",".","."]
  4  [".",".",".",".","X",".",".","."]
  5  [".",".",".",".","B","W",".","."]
  6  [".",".",".",".",".",".","W","."]
  7  [".",".",".",".",".",".",".","B"]

Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
Output: false
Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
 

Constraints:

board.length == board[r].length == 8
0 <= rMove, cMove < 8
board[rMove][cMove] == '.'
color is either 'B' or 'W'.
"""



def checkMove(board, rMove, cMove, color):
    ROWS, COLS = len(board), len(board[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    board[rMove][cMove] = color

    def legal(row, col, color, dir):
        dr, dc = dir
        r, c = row + dr, col + dc
        lenght = 1

        while 0 <= r < ROWS and 0 <= c < COLS:
            lenght += 1
            if board[r][c] == '.':
                return False
            if board[r][c] == color:
                return lenght >= 3
            r, c = r + dr, c + dc
        return False

    for d in directions:
        if legal(rMove, cMove, color, d):
            return True
    return False





#      0   1   2   3   4   5   6   7
#   0  [".",".",".","B",".",".",".","."]
#   1  [".",".",".","W",".",".",".","."]
#   2  [".",".",".","W",".",".",".","."]
#   3  [".",".",".","W",".",".",".","."]
#   4  ["W","B","B","X","W","W","W","B"]
#   5  [".",".",".","B",".",".",".","."]
#   6  [".",".",".","B",".",".",".","."]
#   7  [".",".",".","W",".",".",".","."]

board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
rMove = 4
cMove = 3
color = "B"
output = True

res = checkMove(board, rMove, cMove, color)

print(res)
print(output)