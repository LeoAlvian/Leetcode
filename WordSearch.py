"""
79. Word Search

Solved
Medium
Topics
premium lock icon
Companies

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
      ___________
    [["A","B","C"],"E"]
      -------[   ]
    ["S","F",["C"],"S"]
          ___[   ]
    ["A",["D","E"],"E"]
          -------

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true




Example 2:

    ["A","B","C","E"]
                  ___
    ["S","F","C",["S"]]
              ___[   ]
    ["A","D",["E","E"]]
              -------

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true



Example 3:

    ["A","B","C","E"]
    ["S","F","C","S"]
    ["A","D","E","E"]

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""



# Solving it using Recurrsive and backtrack with time: O(m * 4^n) and space: O(n)

def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    visited = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or word[i] != board[r][c]:
            return False

        visited.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        visited.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True

    return False
        


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
output = True

res = exist(board, word)

print(res)
print(output)