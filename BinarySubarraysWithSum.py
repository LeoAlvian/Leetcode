"""
930. Binary Subarrays With Sum

Solved
Medium
Topics
premium lock icon
Companies

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]



Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""




def numSubarraysWithSum(nums, goal):
    def helper(x):
        if x < 0: 
            return 0

        l, res, cur = 0, 0, 0

        for r in range(len(nums)):
            cur += nums[r]
            while cur > x:
                cur -= nums[l]
                l += 1
            res += (r - l + 1)
        
        return res

    return helper(goal) - helper(goal - 1)


nums = [1,0,1,0,1]
goal = 2
output = 4

print(numSubarraysWithSum(nums, goal))
print(output)