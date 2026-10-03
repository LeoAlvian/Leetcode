"""
215. Kth Largest Element in an Array

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5



Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""



# Using Min Heap with time: O(n logk) and space: O(k)
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Using numpy partition with time O(n) and space: O(n)
from numpy import partition
def findKthLargestII(nums, k):
    return int(partition(nums, -k)[-k])



nums = [3,2,3,1,2,4,5,5,6]
k = 4
output = 4

res = findKthLargest(nums, k)
res2 = findKthLargestII(nums, k)

print(res)
print(res2)
print(output)