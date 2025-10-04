"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3


Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


def majorityEl(nums):
    hashMap = {}
    res, maxCount = 0, 0

    for n in nums:
        hashMap[n] = 1 + hashMap.get(n, 0)
        res = n if hashMap[n] > maxCount else res
        maxCount = max(hashMap[n], maxCount)
    
    return res


nums = [2,2,1,1,1,2,2,1,1]
output = 2
me = majorityEl(nums)
print(me)