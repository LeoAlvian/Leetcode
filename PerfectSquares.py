"""
Docstring for PerfectSquares

279. Perfect Squares

Solved
Medium
Topics
premium lock icon
Companies

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.



Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
"""

# Usind Dynamic Programming to solve this problem with time complexity O(n * n^1/2)
def perfectSquare(n):
    dp = [n] * (n + 1)
    dp[0] = 0

    for target in range(n + 1):
        for s in range(1, target + 1):
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], 1 + dp[target - square])
    
    return dp[n]

n = 12
output = 3
ps = perfectSquare(n)
print(ps)
print(output)