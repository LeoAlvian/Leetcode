"""
2929. Distribute Candies Among Children II

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).



Example 2:

Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

Constraints:

1 <= n <= 106
1 <= limit <= 106
"""

# Inclusion-Exclusion Principle
# We can solve this in constant time using combinatorics

def distributeCandies(n, limit):
    C3 = [1, 3, 3, 1]
    res = 0

    for i in range(4):
        m = n - i * (limit + 1)
        if m < 0:
            continue
        ways = (m + 2) * (m + 1) // 2
        sign = -1 if i % 2 else 1
        res += sign * C3[i] * ways
  
    return res

n = 3
limit = 3
output = 10

res = distributeCandies(n, limit)

print(res)
print(output)