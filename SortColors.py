"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

0 represents red
1 represents white
2 represents blue

Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [1,0,1,2]
Output: [0,1,1,2]


Example 2:
Input: nums = [2,1,0]
Output: [0,1,2]


Example 3:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


def sortColors(nums):
    l, i, r = 0, 0, len(nums) - 1

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while i <= r:
        if nums[i] == 0:
            swap(i, l)
            l += 1
            i += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
        else:
            i += 1



nums = [2,0,2,1,1,0]
output = [0,0,1,1,2,2]
sortColors(nums)
print(nums)
print(output)
print('Is result equal to Output:', nums == output)