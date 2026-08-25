"""
81. Search in Rotated Sorted Array II

Solved
Medium
Topics
premium lock icon
Companies

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true



Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


# Using Modified Binary search with time: O(logn) but in worst case it's gonna be O(n) because there is a duplicate in the array nums and space: O(1)

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2

        if target == nums[m]:
            return True

        # left portion
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        # right portion
        elif nums[l] > nums[m]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

        # the array in the mid is equal to array in the left
        else:
            l += 1

    return False



# Using Hash Set

def searchII(nums, target):
    return True if target in set(nums) else False




nums = [2,5,6,0,0,1,2]
target = 5
output = True

res = search(nums, target)
res2 = searchII(nums, target)

print(res)
print(res2)
print(output)