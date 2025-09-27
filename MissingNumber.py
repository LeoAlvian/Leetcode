"""
Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.

 
Example 1:
Input: nums = [3,0,1]
Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the
missing number in the range since it does not appear in nums.



Example 2:
Input: nums = [0,1]
Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the
missing number in the range since it does not appear in nums.



Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the
missing number in the range since it does not appear in nums.
"""

# This function only works if the number in the list nums doesn't have duplicate 
# and the number in the list nums doesn't exceed n
# Example 
# If the nums = [9,6,13,2,3,5,7,0,1]
# This not gonna work because there's 13 in there which is > n that is 9
def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]
    
    return res


nums = [9,6,4,2,3,5,7,0,1]
output = 8

mn = missingNumber(nums)
print(mn)