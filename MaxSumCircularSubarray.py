"""
Docstring for MaxSumCircularSubarray

918. Maximum Sum Circular Subarray

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.


Example 2:
Input : nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.



Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""


# Kadane's algorithm is an efficient dynamic programming algorithm used to find the 
# maximum sum of a contiguous subarray within a one-dimensional array of numbers. It is 
# known for its simplicity and linear time complexity, O(n), making it faster than 
# brute-force methods. 
# But because we need to find a maximum sum of a circular subarray we need to add a little 
# bit of extra computation 
# Kadane's algorithm is keeping track of curMax and globalMax
# we loop throuth nums and update curMax and globalMax
# curMax = max(curMax + n, n)
# globalMax = max(globalMax, curMax)
# then return globalMax
# But because it's a circular we need to add globalMin, curMin
# curMin = min(curMin + n, n)
# globalMin = min(globalMin, curMin)
# also we need to keep track of the total sum of the arr nums
# when we return we need to consider if all num in nums are negative
# return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
#
# Ex:
#
# nums = [5,-3,5]
#         i
# curMax = 5
# globalMax = 5
# curMin = 5
# globalMin = 5
# total = 5
#
# nums = [5,-3,5]
#            i
# curMax = max(curMax + n, n)          -> max(5 + -3, 5) -> 5
# globalMax = max(globalMax, curMax)   -> max(5 + 5)     -> 5
# curMin = min(curMin + n, n)          -> min(5 + -3, 5) -> 2
# globalMin = min(globalMin, curMin)   -> max(5, 2)      -> 2
# total = 2
#
# nums = [5,-3,5]
#              i
# curMax = max(curMax + n, n)          -> max(5 + 5, 5)  -> 10
# globalMax = max(globalMax, curMax)   -> max(5 + 10)    -> 10
# curMin = min(curMin + n, n)          -> min(2 + 5, 5)  -> 5
# globalMin = min(globalMin, curMin)   -> max(2, 5)      -> 2
# total = 7
#
# because globalMax > 0
# return max(globalMax, total - globalMin) -> max(10, 7 - 2) -> 10

def maxSumCircularSubarray(nums):
    globalMax, globalMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0

    for n in nums:
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globalMax = max(globalMax, curMax)
        globalMin = min(globalMin, curMin)
    
    return max(globalMax, total - globalMin) if globalMax > 0 else globalMax


nums = [5,-3,5]
output = 10
mscs = maxSumCircularSubarray(nums)
print(mscs)
print(output)