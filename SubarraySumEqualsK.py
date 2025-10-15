"""
560. Subarray Sum Equals K - Explanation

You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,-1,1,2], k = 2
Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.


Example 2:
Input: nums = [4,4,4,4,4,4], k = 4
Output: 6


Constraints:

1 <= nums.length <= 20,000
-1,000 <= nums[i] <= 1,000
-10,000,000 <= k <= 10,000,000
"""

"""
[2,-1,1,2]
count=0
res=0
prefix = {0:1}

How to solve

[2,-1,1,2]
 i
count= i-k = 2-3 = -1, if -1 in prefix get the count and add it to res else put i to prefix with count 1
res=0
prefix = {0:1}
         {2:1}

[2,-1,1,2]
    i
count= i-k = -1-3 = -4, if -4 in prefix get the count and add it to res else put i to prefix with count 1
res=0
prefix = { 0:1}
         { 2:1}
         {-1:1}

[2,-1,1,2]
      i
count= i-k = 1-3 = -2, if -2 in prefix get the count and add it to res else put i to prefix with count 1
res=0
prefix = { 0:1}
         { 2:1}
         {-1:1}
         {-2:1}

[2,-1,1,2]
        i
count= i-k = 2-3 = -1, if -1 in prefix get the count and add it to res else put i to prefix with count 1
res=1+{-1:1} = 1 + 1 = 2
prefix = { 0:1}
         { 2:1}
         {-1:1}
         {-2:1}
"""

def subArrSumK(nums, k):
    res = 0
    count = 0
    prefix = { 0 : 1 }

    for n in nums:
        count += n
        if count - k in prefix:
            res += prefix[count - k]
        prefix[count] = 1 + prefix.get(count, 0)
    
    return res


nums = [2,-1,1,2]
k = 2
output = 4

sas = subArrSumK(nums, k)
print(sas)
print(output)