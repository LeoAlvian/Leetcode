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
# i : 1, num : 2
# val = dp[1]*dp[1] = 1 * 1 = 1
# dp[2] : max(2, 1)
# dp : {1: 1, 2: 2}

# i : 1, num : 3
# val = dp[1]*dp[2] = 1 * 2 = 2
# dp[3] : max(3, 2)
# dp : {1: 1, 2: 2, 3: 3}

# i : 2, num : 3
# val = dp[2]*dp[1] = 2 * 1 = 2
# dp[3] : max(3, 2)
# dp : {1: 1, 2: 2, 3: 3}

# i : 1, num : 4
# val = dp[1]*dp[3] = 1 * 3 = 3
# dp[4] : max(4, 3)
# dp : {1: 1, 2: 2, 3: 3, 4: 4}

# i : 2, num : 4
# val = dp[2]*dp[2] = 2 * 2 = 4
# dp[4] : max(4, 4)
# dp : {1: 1, 2: 2, 3: 3, 4: 4}

# i : 3, num : 4
# val = dp[3]*dp[1] = 3 * 1 = 3
# dp[4] : max(4, 3)
# dp : {1: 1, 2: 2, 3: 3, 4: 4}

# i : 1, num : 5
# val = dp[1]*dp[4] = 1 * 4 = 4
# dp[5] : max(4, 4)
# dp : {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}

# i : 2, num : 5
# val = dp[2]*dp[3] = 2 * 3 = 6
# dp[5] : max(6, 6)
# dp : {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}

# i : 3, num : 5
# val = dp[3]*dp[2] = 3 * 2 = 6
# dp[5] : max(6, 6)
# dp : {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}

# i : 4, num : 5
# val = dp[4]*dp[1] = 4 * 1 = 4
# dp[5] : max(6, 4)
# dp : {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}


def intBreak(n):
    dp = { 1 : 1 }

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            val = dp[i] * dp[num - i]
            dp[num] = max(dp[num], val)
    
    return dp[n]

# Using Math

def integerBreakMath(n):
    if n <= 3:
        return n - 1

    res = 3 ** (n // 3)
    # print('res', res)
    # print('mod', n % 3)
    if n % 3 == 1:
        # print('mod res', (res // 3) * 4)
        return (res // 3) * 4
    
    
    # print(f'mod 2 = {res} * max(1, {(n % 3)}) = {res * max(1, (n % 3))}')
    return res * max(1, (n % 3))

n = 10
output = 36
ib = intBreak(n)
ibm = integerBreakMath(n)
print('Dynamic',ib)
print('Math', ibm)
print(output)