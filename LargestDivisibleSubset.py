"""
368. Largest Divisible Subset

Solved
Medium
Topics
premium lock icon
Companies

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.




Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""




def largestDivisibleSubset(nums):
    nums.sort()
    N = len(nums)
    dp = [[num] for num in nums]
    # dp = [[1], [2], [5], [15], [45]]
    res = []

    for i in reversed(range(N)):
        for j in range(i + 1, N):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dp[j]
                dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
                # dp = [[1, 5, 15, 45], [2], [5, 15, 45], [15, 45], [45]]
        res = dp[i] if len(dp[i]) > len(res) else res
    
    return res



nums = [1, 2, 5, 15, 45]
output = [1, 5, 15, 45]

res = largestDivisibleSubset(nums)

print(res)
print(output)