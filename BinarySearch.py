"""
704. Binary Search

Solved
Easy
Topics
premium lock icon
Companies

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4



Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


# Solve Using binary search with time: O(logn) and space: O(1)

def search(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = l + ((r - l) // 2)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
        else:
            return mid

    return -1


nums = [-1,0,3,5,9,12]
target = 9
output = 4

bs = search(nums, target)

print(bs)
print(output)