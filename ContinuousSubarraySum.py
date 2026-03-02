"""
523. Continuous Subarray Sum

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 


Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.



Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.



Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false



Example 4:
nums = [23,2,4,6,6]
k = 7
output = True



Example 5:
nums = [2,4,3]
k = 6
output = True
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""


# We solve this problem by building a hash map with reminder as a key and index of the 
# reminder and then check if the remindier is already in hash map, if it is and the 
# index of that minus the index of the same reminder is bigger than 2 we can return True
#
# Ex:
#
# nums = [23,2,4,6,6]
# k = 7
# 
# nums  = [23,2,4,6,6]
# index =   i
# remainIdxMap = { 0 : -1 } we use a default value because of this problem specivicaly
# total += nums[i] = 0 + 23 = 23
# remainder = 23 % 7 = 2
# remainIdxMap = { 0 : -1 }
#                { 2 :  0 }
#
# nums  = [23,2,4,6,6]
# index =     i
# total += nums[i] = 23 + 2 = 25
# remainder = 25 % 7 = 4
# remainIdxMap = { 0 : -1 }
#                { 2 :  0 }
#                { 4 :  1 }
#
# nums  = [23,2,4,6,6]
# index =       i
# total += nums[i] = 25 + 4 = 29
# remainder = 29 % 7 = 1
# remainIdxMap = { 0 : -1 }
#                { 2 :  0 }
#                { 4 :  1 }
#                { 1 :  2 }
#
# nums  = [23,2,4,6,6]
# index =         i
# total += nums[i] = 29 + 6 = 35
# remainder = 35 % 7 = 0, 0 is in remainIdxMap, we calculate if cur idx which is 3 
# minus remainIdxMap[0] which is -1 => 3 - -1 = 4 which is bigger than 2 than we return 
# True, and the starting index of that is -1 + 1 = 0, the end 3 + 1 = 4
# so nums[0:4] is add up to multiple of 7 
# nums = [23,2,4,6] with sum of 35
# remainIdxMap = { 0 : -1 }  <-
#                { 2 :  0 }
#                { 4 :  1 }
#                { 1 :  2 }



def checkSubarraySum(nums, k):
    remainIdxMap = { 0 : -1 }
    total = 0

    for i, n in enumerate(nums):
        total += n
        r = total % k 
        if r not in remainIdxMap:
            remainIdxMap[r] = i
        elif i - remainIdxMap[r] > 1:
            return (True, remainIdxMap[r] + 1, i + 1)
    
    return (False, 0, 0)


nums = [23,2,4,6,6]
k = 7
output = True

res, start, end = checkSubarraySum(nums, k)
print(res)
print(nums[start:end])
print(sum(nums[start:end]))
print(output)