"""
2206. Divide Array Into Equal Pairs

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.



Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

Constraints:

nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""

from collections import Counter
# Using Counter built in method and the fastest on leetcode
# Couter output are hash map with element as keys and count as values
def divideArray(nums):
    count = Counter(nums)
    
    for c in count.values():
        if c % 2:
            return False
    
    return True


# Using hash set 
def divideArrayII(nums):
    odd_set = set()

    for n in nums:
        if n not in odd_set:
            odd_set.add(n)
        else:
            odd_set.remove(n)
    
    return not len(odd_set)


# Using hash map manually
def divideArrayIII(nums):
    count = {}

    for n in nums:
        if n not in count:
            count[n] = 0
        count[n] += 1
    
    for c in count.values():
        if c % 2:
            return False
    
    return True




nums = [3,2,3,2,2,2]
output = True

res = divideArray(nums)
res2 = divideArrayII(nums)
res3 = divideArrayIII(nums)

print(res)
print(res2)
print(res3)
print(output)