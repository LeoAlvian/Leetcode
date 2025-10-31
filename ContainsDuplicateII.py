"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true



Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true



Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

# Using sliding window algorith and set to store num
# Ex
# nums = [1, 0, 1, 1]
# k = 1
# window = {}
# nums = [1, 0, 1, 1]
#         lr            sliding window and check if r in window and r - l > k if not add nums[r] to window
# window = {1}
# nums = [1, 0, 1, 1]
#         l  r          sliding window and check if r in window and r - l > k if not  add nums[r] to window
# window = {1,2}
# nums = [1, 0, 1, 1]
#         l     r       sliding window and check if r in window and r - l > k if not  add nums[r] to window
# window = {1,2,3}
# nums = [1, 0, 1, 1]
#         l        r    sliding window and check if r in window and r - l > k if not  add nums[r] to window
# window = {1,2,3} in this case nums[r] = 1 and 1 is indeed in window and r - l > k so we return True
def containsDuplicateII(nums, k):
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False


# Using hashmap is slightly faster but the core algorith are still the same
def containDuplicateIIHashMap(nums, k):
    hash = {}
    
    for i, n in enumerate(nums):
        if n in hash and i - hash[n] <= k:
            return True
        hash[n] = i
    return False


nums = [1,0,1,1]
k = 1
output = True
cd = containsDuplicateII(nums, k)
print(cd)
print(output)
cdh = containDuplicateIIHashMap(nums, k)
print(cdh)