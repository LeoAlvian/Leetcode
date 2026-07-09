"""
34. Find First and Last Position of Element in Sorted Array

Solved
Medium
Topics
premium lock icon
Companies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]



Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]



Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


def searchRange(nums, target):
    left = binSearch(nums, target, True)
    right = binSearch(nums, target, False)
    return [left, right]


def binSearch(nums, target, leftBias):
    l, r = 0, len(nums) - 1
    i = -1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    
    return i



nums = [5,7,7,8,8,10]
target = 8
output = [3,4]

res = searchRange(nums, target)

print(res)
print(output)