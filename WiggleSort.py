"""
280. Wiggle Sort - Explanation

Description
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.



Example 1:
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.



Example 2:
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]



Example 3:
Input: nums = [1,2,3,4,5,6,7]
Output: [1,3,2,5,4,7,6]



Constraints:

1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 10^4
It is guaranteed that there will be an answer for the given input nums.

Follow Up: Could you solve the problem in O(n) time complexity?
"""

# We need to edit the array in place and we gonna achieve time complexity of O(n)
# which means we cannot sort the array first because it's gonna be O(n logn)

def wiggleSort(nums):
    for i in range(1, len(nums)):
        if (i % 2 and nums[i] < nums[i - 1]) or (not i % 2 and nums[i] > nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    
    return nums



nums = [1,2,3,4,5,6,7]
output = [1,3,2,5,4,7,6]


print(wiggleSort(nums))
print(output)