"""
238. Product of Array Except Self
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]



Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

def productExceptSelf(nums):
    res = [1] * (len(nums))

    prefix = 1
    print(f'res[i] = prefix -> prefix *= nums[i]')
    for i in range(len(nums)):
        res[i] = prefix
        # print(f'res[{i}] = prefix = {prefix}')
        # print(f'prefix *= nums[{i}] = {prefix} * {nums[i]} = {prefix * nums[i]}')
        prefix *= nums[i]
    # res[0] = prefix = 1
    # prefix *= nums[0] = 1 * 1 = 1
    # res[1] = prefix = 1
    # prefix *= nums[1] = 1 * 2 = 2
    # res[2] = prefix = 2
    # prefix *= nums[2] = 2 * 4 = 8
    # res[3] = prefix = 8
    # prefix *= nums[3] = 8 * 6 = 48
    # first prefix res = [1, 1, 2, 8]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        # print(f'res[{i}] = {res[i]}, postfix= {postfix}')
        # print(f'res = {res}')
        # print(f'res[{i}] = postfix *= nums[{i}] = {postfix} * {nums[i]} = {postfix * nums[i]}')
        postfix *= nums[i]
    # print(f'second postfix res = {res}')
    # res[3] = postfix *= nums[3] = 1 * 6 = 6
    # res[2] = postfix *= nums[2] = 6 * 4 = 24
    # res[1] = postfix *= nums[1] = 24 * 2 = 48
    # res[0] = postfix *= nums[0] = 48 * 1 = 48
    # second postfix res = [48, 24, 12, 8]
    
    return res
        
        
nums = [1,2,4,6]
output = [48,24,12,8]

print(productExceptSelf(nums))
print(output)