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

# Use backtrack to find all posible solutions
#
# Ex:
# 
# n = 4 -> output = 2
# 
# First we gonna brute force every possible solution using backtrack 
# we gonna place queen and check if the next queen is possible to be placed, 
# if not we gonna backtrack and choose another path
#
#   0 1 2 3
# 0[Q,_,_,_]   -> we place the queen on the r = 0 and c = 0
# 1[_,_,_,_]
# 2[_,_,_,_]
# 3[_,_,_,_]
#
#   0 1 2 3
# 0[Q,x,x,x]   -> then we crossed out horizontal, vertical, and diagola spot,
# 1[x,x,Q,_]   -> then we place the next queen on the possible spot such as 
# 2[x,_,x,_]   -> r = 1 and c = 2
# 3[x,_,_,x]
#
#   0 1 2 3
# 0[Q,x,x,x]   -> then we crossed out horizontal, vertical, and diagola spot,
# 1[x,x,Q,x]   -> as you can see we cannot place the next queen because there is 
# 2[x,x,x,x]   -> no possible spot on the 2nd row so we backtrack
# 3[x,_,x,x]
#
# We keep backtrack it until we find solution which is 2 possible setup, which is
#     1st              2nd
#   0 1 2 3          0 1 2 3
# 0[_,Q,_,_]       0[_,_,Q,_]  
# 1[_,_,_,Q]       1[Q,_,_,_] 
# 2[Q,_,_,_]       2[_,_,_,Q] 
# 3[_,_,Q,_]       3[_,Q,_,_]
#
# We use set of col to keep track of col that are not allowed to put the next queen is
# And set of negative Diagonal or negDiag to keep track of negative diagonal that 
# are not allowed to put the next queen in this case is (r - c), if r - c are equal 
# which means the we are in the same negative diagonal 
# ex: 
#
# r = 1, c = 2 -> r - c -> 1 - 2 = -1                    
#   0 1 2 3          
# 0[_,_,_,_]         
# 1[_,_,Q,_]       
# 2[_,_,_,_]       
# 3[_,_,_,_]    
#    
# r = 0, c = 1 -> r - c -> 0 - 1 = -1                    
#   0 1 2 3          
# 0[_,Q,_,_]         
# 1[_,_,Q,_]       
# 2[_,_,_,_]       
# 3[_,_,_,_]  
#
# r = 2, c = 3 -> r - c -> 2 - 3 = -1                
#   0 1 2 3          
# 0[_,Q,_,_]         
# 1[_,_,Q,_]       
# 2[_,_,_,Q]       
# 3[_,_,_,_]  
# And set of positive Diagonal or posDiag to keep track of positive diagonal that 
# are not allowed to put the next queen in this case is (r + c) if r + c are equal 
# which means the we are in the same positive diagonal
# ex: 
#
# r = 1, c = 2 -> r + c -> 1 + 2 = 3                    
#   0 1 2 3          
# 0[_,_,_,_]         
# 1[_,_,Q,_]       
# 2[_,_,_,_]       
# 3[_,_,_,_]    
#    
# r = 2, c = 1 -> r + c -> 2 + 1 = 3                    
#   0 1 2 3          
# 0[_,_,_,_]         
# 1[_,_,Q,_]       
# 2[_,Q,_,_]       
# 3[_,_,_,_]  
#
# r = 0, c = 3 -> r + c -> 0 + 3 = 3                
#   0 1 2 3          
# 0[_,_,_,Q]         
# 1[_,_,Q,_]       
# 2[_,Q,_,_]       
# 3[_,_,_,_]  


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