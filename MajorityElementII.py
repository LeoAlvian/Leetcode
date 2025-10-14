"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


Example 1:
Input: nums = [3,2,3]
Output: [3]


Example 2:
Input: nums = [5,2,3,2,2,2,2,5,5,5]
Output: [2,5]


Example 3:
Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
"""

from collections import defaultdict

def majorityEl2Hash(nums):
    count = defaultdict(int)

    for n in nums:
        count[n] += 1
        if len(count) <= 2:
            continue

        new_count = defaultdict(int)
        for n, c in count.items():
            if c > 1:
                new_count[n] = c - 1
        count = new_count

    res = []
    for n in count:
        if nums.count(n) > len(nums) // 3:
            res.append(n)
    return res


nums = [5,2,3,2,2,2,2,5,5,5]
output = [2,5]
me2h = majorityEl2Hash(nums)
print(me2h)
print(output)