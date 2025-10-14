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

# This method using hash map and remove element if the lenght of it are exceeding 2
# and decrease the counter as well
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


# Using Boyer Moore Algorithm to count the majority element with O(1) space complexity
# this work by counting element that are similar and decrement it if it isn't 
# and if the count are 0 we gonna replace that element with the new one
# We gonna use two variable to hold majority number and two variable to hold 
# the count, after we count the majority element we gonna reset both count to 0
# and recount how many number the element appear, then we gonna append it to res
# if the count > len(nums) // 3, then return res

def majorityEl2BoyerMoore(nums):
    maj1, maj2, count1, count2 = 0, 0, 0, 0
    n = len(nums)

    for num in nums:
        if num == maj1:
            count1 += 1
        elif num == maj2:
            count2 += 1
        elif count1 == 0:
            maj1 = num
            count1 = 1
        elif count2 == 0:
            maj2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1, count2 = 0, 0
    for num in nums:
        if num == maj1:
            count1 += 1
        elif num == maj2:
            count2 += 1
    
    res = []
    if count1 > n // 3:
        res.append(maj1)
    if count2 > n // 3:
        res.append(maj2)
    return res


nums = [5,2,3,2,2,2,2,5,5,5]
output = [2,5]
me2h = majorityEl2Hash(nums)
print(me2h)
print(output)
print('==================')
me2bm = majorityEl2BoyerMoore(nums)
print(me2bm)
print(output)