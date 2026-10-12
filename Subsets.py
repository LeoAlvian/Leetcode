"""
78. Subsets

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]



Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


# Solving it using backtrack or DFS with time: O(n * 2^n) and space: O(n) extra space and O(2^n) for the output

def subsets(nums):
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Including the nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Not including nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res 


# Solving it iteratively with time: O(n * 2^n) and space: O(n) for the extra space and O(2^n) for the output

def subsetsIteration(nums):
    res = [[]]

    for num in nums:
        temp = []
        for subset in res:
            subset = subset + [num]
            temp.append(subset)
        res += temp

    return res



nums = [1,2,3]
output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

res = subsets(nums)
res2 = subsetsIteration(nums)

print(res)
print(res2)
print(output)