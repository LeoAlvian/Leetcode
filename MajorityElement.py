"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3


Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# Using hash map to map all element in the arr and count how many they are 
# appearing ex {1:2, 2:1, 3:4} which means 3 is the majority element here 
# but this approach are using O(n) space and O(n) time complexity 
def majorityElHash(nums):
    hashMap = {}
    res, maxCount = 0, 0

    for n in nums:
        hashMap[n] = 1 + hashMap.get(n, 0)
        res = n if hashMap[n] > maxCount else res
        maxCount = max(hashMap[n], maxCount)
    
    return res


# Using Boyer Moore Algorithm to count the majority element with O(1) space complexity
# this work by counting element that are similar and decrement it if it isn't 
# and if the count are 0 we gonna replace that element with the new one
# ex: nums= [1,2,1]
# count == 0 so change the res to be the first element which is 1 so res = 1 
# and count == 1, then we see 2 which is different element so we decrement count = 0
# then the count = 0 and the next element is 1 so we put 1 to res so res = 1
def majorityEl(nums):
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += 1 if n == res else -1
    
    return res


nums = [2,2,1,1,1,2,2]
output = 2
meh = majorityElHash(nums)
print(meh)
me = majorityEl(nums)
print('Withouth Hash', me)