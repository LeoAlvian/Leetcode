"""
52. N-Queens II
Solved
Hard
Topics
premium lock icon
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 
Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.


Example 2:
Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
"""


def nQueensII(n):
    col = set()
    negDiag = set() # (r - c)
    posDiag = set() # (r + c)
    res = 0

    def backtrack(r):
        if r == n:
            nonlocal res
            res += 1
            return
        for c in range(n):
            if c in col or (r - c) in negDiag or (r + c) in posDiag:
                continue
            
            col.add(c)
            negDiag.add(r - c)
            posDiag.add(r + c)
            backtrack(r + 1)
            col.remove(c)
            negDiag.remove(r - c)
            posDiag.remove(r + c)
    
    backtrack(0)
    return res

n = 4
output = 2
nq2 = nQueensII(n)
print(nq2)
print(output)