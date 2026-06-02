"""
645. Set Mismatch

Solved
Easy
Topics
premium lock icon
Companies

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]



Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""


# Solving with Negative Marking with time: O(n) and space: O(1)
def findErrorNums(nums):
    res = [0, 0]

    for num in nums:
        num = abs(num)
        nums[num - 1] *= -1
        if nums[num - 1] > 0:
            res[0] = num
    
    for i, num in enumerate(nums):
        if num > 0 and i + 1 != res[0]:
            res[1] = i + 1
            return res

nums = [1,2,2,4]
output = [2,3]

res = findErrorNums(nums)

print(res)
print(output)