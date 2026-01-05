"""
Docstring for LastStoneWeightII

1049. Last Stone Weight II

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.



Example 2:
Input: stones = [31,26,33,21,40]
Output: 5
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 100
"""

import time


# Recursive using DFS
def lastStoneWeightII(stones):
    stoneSum = sum(stones)
    target = stoneSum // 2
    dp = {}

    def dfs(i, total):
        if i == len(stones) or total >= target:
            return abs(total - (stoneSum - total))
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
        return dp[(i, total)]

    return dfs(0, 0)


# Using Array for the dynamic programming
def lastStnWeightII(stones):
    stoneSum = sum(stones)
    target = stoneSum // 2
    dp = [False] * (target+1)
    dp[0] = True
    # print('dp',dp)

    for stone in stones:
        for i in range(target - stone, -1, -1):
            if dp[i]:
                dp[i + stone] = True
    # print('dp loop',dp)
    
    for i in range(target, -1, -1):
        if dp[i]:
            # print(f'stoneSum : {stoneSum} - (2 * i) : {(2*i)} = {stoneSum - (2 * i)}')
            return stoneSum - (2 * i)
        


stones = [31,26,33,21,40]
output = 5
t0 = time.time()
lsw = lastStoneWeightII(stones)
t1 = time.time()
t2 = time.time()
ls = lastStnWeightII(stones)
t3 = time.time()
print('Recursive', lsw)
print('DP', ls)
print(output)
print(t1 - t0)
print(t2 - t3)