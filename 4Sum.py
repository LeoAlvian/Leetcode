"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]



Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]



Example 3:

Input: nums = [3,2,3,-3,1,0], target = 3
Output: [[-3,0,3,3],[-3,1,2,3]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

# Solution

"""
This problem is a follow-up of 3Sum, so take a look at that problem first if you haven't. 4Sum and 3Sum are very similar; the difference is that we are looking for unique quadruplets instead of triplets.

As you see, 3Sum just wraps Two Sum in an outer loop. As it iterates through each value v, it finds all pairs whose sum is equal to target - v using one of these approaches:

Two Sum uses a hash set to check for a matching value.
Two Sum II uses the two pointers pattern in a sorted array.
Following a similar logic, we can implement 4Sum by wrapping 3Sum in another loop. But wait - there is a catch. If an interviewer asks you to solve 4Sum, they can follow-up with 5Sum, 6Sum, and so on. What they are really expecting at this point is a kSum solution. Therefore, we will focus on a generalized implementation here.

Approach 1: Two Pointers
Intuition

The two pointers pattern requires the array to be sorted, so we do that first. Also, it's easier to deal with duplicates if the array is sorted: repeated values are next to each other and easy to skip.

For 3Sum, we enumerate each value in a single loop, and use the two pointers pattern for the rest of the array. For kSum, we will have k - 2 nested loops to enumerate all combinations of k - 2 values."""

# Algorithm

""" 

We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters. When k == 2, we will call twoSum, terminating the recursion.

For the main function:

Sort the input array nums.
Call kSum with start = 0, k = 4, and target, and return the result.
For kSum function:

At the start of the kSum function, we will check three conditions:
Have we run out of numbers to choose from?
Is the smallest number remaining greater than target / k?
If so, then any k numbers we choose will be too large.
Is the largest number remaining smaller than target / k?
If so, then any k numbers we choose will be too small.
If any of these conditions is true, there is no need to continue as no combination of the remaining elements can sum to target.
If k equals 2, call twoSum and return the result.
Iterate i through the array from start:
If the current value is the same as the one before, skip it.
Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
For each returned subset of values:
Include the current value nums[i] into subset.
Add subset to the result res.
Return the result res.
For twoSum function:

Set the low pointer lo to start, and high pointer hi to the last index.
While low pointer is smaller than high:
If the sum of nums[lo] and nums[hi] is less than target, increment lo.
Also increment lo if the value is the same as for lo - 1.
If the sum is greater than target, decrement hi.
Also decrement hi if the value is the same as for hi + 1.
Otherwise, we found a pair:
Add it to the result res.
Decrement hi and increment lo.
Return the result res
"""


def s4Sum(nums, target):
    nums.sort()
    res, quad = [], []

    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return

        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    
    kSum(4, 0, target)
    return res



nums = [1,0,-1,0,-2,2] 
target = 0
output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
s = s4Sum(nums, target)
print(s)
print(output)