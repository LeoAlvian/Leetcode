"""
Docstring for CombinationSumIV

377. Combination Sum IV

Solved
Medium
Topics
premium lock icon
Companies

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.



Example 2:
Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
"""


# Using Dynamic Programming with top-down approach
# nums = [1,2,3]
# target = 4
# output = 7
#
# we initialaize dp = { 0 : 1 }
# loop from 1 to target
# loop through all nums
# compute and add all values in dp[i - num] to dp[i]
#
# nums = [1,2,3]
# i 1
# {0: 1, 1: 1}    -> dp[i] += dp[i - nums[0]] -> dp[1 - 1] = dp[0] = 1 -> dp[1] = 1
# {0: 1, 1: 1}    -> dp[1] -> dp[1 - 2] = dp[-1] is not exist so dp[1] still 1
# {0: 1, 1: 1}    -> dp[1] -> dp[1 - 3] = dp[-2] is not exist so dp[1] still 1
# i 2
# {0: 1, 1: 1, 2: 1} -> dp[2] -> dp[2 - 1] = dp[1] = 1 -> dp[2] = 1
# {0: 1, 1: 1, 2: 2} -> dp[2] -> dp[2 - 2] = dp[0] = 1 -> dp[2] = 1 + 1 = 2
# {0: 1, 1: 1, 2: 2} -> dp[2] -> dp[2 - 3] = dp[-1] is not exist so dp[2] still 2
# i 3
# {0: 1, 1: 1, 2: 2, 3: 2} -> dp[3] -> dp[3 - 1] = dp[2] = 2 -> dp[3] = 2
# {0: 1, 1: 1, 2: 2, 3: 3} -> dp[3] -> dp[3 - 2] = dp[1] = 1 -> dp[3] = 2 + 1 = 3
# {0: 1, 1: 1, 2: 2, 3: 4} -> dp[3] -> dp[3 - 3] = dp[0] = 1 -> dp[3] = 3 + 1 = 4
# i 4
# {0: 1, 1: 1, 2: 2, 3: 4, 4: 4} -> dp[4] -> dp[4 - 1] = dp[3] -> 4 -> dp[4] = 4
# {0: 1, 1: 1, 2: 2, 3: 4, 4: 6} -> dp[4] -> dp[4 - 2] = dp[2] = 2 -> dp[4] = 4 + 2 = 6
# {0: 1, 1: 1, 2: 2, 3: 4, 4: 7} -> dp[4] -> dp[4 - 3] = dp[1] = 1 -> dp[4] = 6 + 1 = 7
#
# Then we return dp[target] = dp[4] = 7

def combSumIV(nums, t):
    dp = { 0 : 1 }

    for i in range(1, t + 1):
        dp[i] = 0
        for n in nums:
            dp[i] += dp.get(i - n, 0)
    
    return dp[t]


nums = [1,2,3]
target = 4
output = 7
cs = combSumIV(nums, target)
print(cs)
print(output)