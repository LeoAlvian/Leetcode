"""
179. Largest Number

Solved
Medium
Topics
premium lock icon
Companies

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:
Input: nums = [10,2]
Output: "210"



Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"



Example 3:
Input: nums = [0,0,0,0,0]
output = '0'

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""


from functools import cmp_to_key

def largestNum(nums):
    # convert all value in nums to str
    nums = list(map(str, nums))
    # from nums = [3,30,34,5,9] to
    # nums = ['3', '30', '34', '5', '9']

    # Sort using built-in function that return first element if a + b > b + a else 
    # return second element
    nums.sort(key = cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
    # nums = ['9', '5', '34', '3', '30']

    # to handle edge case where nums = [0,0,0,0] we need to return just '0' not '0000'
    return '0' if nums[0] == '0' else ''.join(nums)




nums = [3,30,34,5,9]
output = "9534330"


print(largestNum(nums))
print(output)