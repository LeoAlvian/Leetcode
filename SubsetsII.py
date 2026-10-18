"""
90. Subsets II

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]



Example 2:

Input: nums = [1,2,2,3]
Output: [[], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], [1, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]]



Example 3:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


# Solving it using backtrack with time: O(n * 2^n) and space: O(n)

def subsetsWithDup(nums):
    res = []
    nums.sort()

    def backtrack(start, path):
        res.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res


nums = [1,2,2,3]
output = [[], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], [1, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]]

res = subsetsWithDup(nums)

print(res)
print(output)