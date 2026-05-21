"""
1512. Number of Good Pairs

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.



Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.



Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from collections import Counter
# Mathematical Way of solving this problem with time: O(n) and space: O(n)
def numIdenticalPairs(nums):
    count = Counter(nums)
    res = 0

    for n, c in count.items():
        res += c * (c - 1) // 2
    
    return res


# Solve it algorithmicly 
def numIdenticalPairsII(nums):
    res = 0
    count = {}

    for n in nums:
        if n in count:
            res += count[n]
            count[n] += 1
        else:
            count[n] = 1
    
    return res


nums = [1,2,3,1,1,3]
output = 4

res = numIdenticalPairs(nums)
res2 = numIdenticalPairsII(nums)

print(res)
print(res2)
print(output)