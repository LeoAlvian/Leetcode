"""
130. Surrounded Regions

Solved
Medium
Topics
premium lock icon
Companies

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

    ["X","X","X","X"]       ["X","X","X","X"]
    ["X","O","O","X"]       ["X","X","X","X"] 
    ["X","X","O","X"]       ["X","X","X","X"] 
    ["X","O","X","X"]       ["X","O","X","X"]

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.




Example 2:

Input: board = [["X"]]
Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


# Solve using DFS with time: O(m * n) and space: O(m * n)

def  surroundedRegions(board):
    ROWS, COLS = len(board), len(board[0])
    visit = set()

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O' or (r, c) in visit:
            return 

        visit.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                dfs(r, c)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O' and (r, c) not in visit:
                board[r][c] = 'X'



# Using BFS with faster time complexity on leetcode but time still O(m * n) and space: O(m * n)
from collections import deque

def surroundedRegionsBFS(board):
    ROWS, COLS = len(board), len(board[0])
    q = deque()
    # visit = set()
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # collect every border 'O' as a starting point
    for r in range(ROWS):
        for c in [0, COLS - 1]:
            if board[r][c] == 'O':
                board[r][c] = 'T'
                q.append((r, c))
                # visit.add((r, c))

    for c in range(COLS):
        for r in [0, ROWS - 1]:
            if board[r][c] == 'O':
                board[r][c] = 'T'
                q.append((r, c))
                # visit.add((r, c))

    # mark everything connected to the border
    while q:
        qr, qc = q.popleft()
        for dr, dc in directions:
            r, c = qr + dr, qc + dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                # visit.add((r, c))
                board[r][c] = 'T'
                q.append((r, c))

    # surrounded → 'X', border-connected → back to 'O'
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'


    



    # ["X","X","X","X"]       ["X","X","X","X"]
    # ["X","O","O","X"]       ["X","X","X","X"] 
    # ["X","X","O","X"]       ["X","X","X","X"] 
    # ["X","O","X","X"]       ["X","O","X","X"]


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board2 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

surroundedRegions(board)
surroundedRegionsBFS(board2)


print(board)
print(board2)
print(output)