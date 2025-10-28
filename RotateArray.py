"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]



Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


# Modify nums in place with O(1) space complexity and O(n) times complexity
def rotateArr(nums, k):

    # Helper functoin to reverse the list
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    # Mod k in case k is bigger than len nums
    k = k % len(nums)

    # Rotate all nums so 
    # nums = [1,2,3,4,5,6,7] 
    # nums = [7,6,5,4,3,2,1]
    l, r = 0, len(nums) - 1
    reverse(l, r)

    # Rotate nums from the start to k - 1 because it is inclusive
    # nums = [7,6,5,4,3,2,1]
    # nums = [5,6,7,4,3,2,1]
    l, r = 0, k - 1
    reverse(l, r)

    # Rotate nums from k to end of nums - 1
    # nums = [5,6,7,4,3,2,1]
    # nums = [5,6,7,1,2,3,4]
    l, r = k, len(nums) - 1
    reverse(l, r)

    return nums



nums = [1,2,3,4,5,6,7]
k = 3
output = [5,6,7,1,2,3,4]
ra = rotateArr(nums, k)
print(output)
print(ra)