"""
Docstring for TwoSumII

167. Two Sum II - Input Array Is Sorted

Solved
Medium
Topics
premium lock icon
Companies

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].



Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].



Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""


# Because this arr numbers are already sorted we can use two pointer
# Using two pointer solution, we gonna assing l to be 0 and r to len(nums) - 1
# loop until we find target, if current sum is smaller we increase l, if larger
# we decrease r, if we find the target return in a list of 1-indexed
# If we didn't find the target return []
# Time complexity is O(n), and space complexity is O(1)
def twoSumII(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        curSum = nums[l] + nums[r]
        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l + 1, r + 1]
    
    return []


numbers = [2,7,11,15]
target = 9
output = [1,2]

ts = twoSumII(numbers, target)

print(ts)
print(output)