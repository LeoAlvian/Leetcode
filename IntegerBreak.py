"""
Docstring for IntegerBreak

343. Integer Break

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 x 1 = 1.


Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 x 3 x 4 = 36.
 

Constraints:

2 <= n <= 58
"""

# Using Dynamic Programming

def intBreak(n):
    dp = { 1 : 1 }

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            val = dp[i] * dp[num - i]
            dp[num] = max(dp[num], val)
    
    return dp[n]

n = 10
output = 36
ib = intBreak(n)
print(ib)
print(output)