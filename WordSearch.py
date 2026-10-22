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




# You need to update Python to 3.10 or above to run this function

from collections import Counter
from itertools import chain, product

def existII(board, word):
    m, n = len(board), len(board[0])
    
    if len(word) > m * n: return False                       # [a] trivial case to discard

    cnt = Counter(word)
    if not (cnt) <= Counter(chain(*board)):                  # [b] there are not enough
        return False                                         #     letters on the board
    
    if cnt[word[0]] > cnt[word[-1]]:                         # [c] inverse word if it's better
            word = word[::-1]                                #     to start from the end
    
    def dfs(i, j, s):                                        # recursive postfix search
        
        if s == len(word) : return True                      # [1] found the word
        
        if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:  # [2] found a letter
            board[i][j] = "#"                                     # [3] mark as visited
            adj = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]               # [4] iterate over adjacent cells...
            dp = any(dfs(ii,jj,s+1) for ii,jj in adj)             # [5] ...and try next letter
            board[i][j] = word[s]                                 # [6] remove mark
            return dp                                             # [7] return search result

        return False                                              # [8] this DFS branch failed
            
    return any(dfs(i,j,0) for i,j in product(range(m),range(n)))
        


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
output = True

res = exist(board, word)
# res2 = existII(board, word)

print(res)
# print(res2)
print(output)