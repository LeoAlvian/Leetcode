"""

485. Max Consecutive Ones

Easy
Topics
premium lock icon
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.



Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""



def maxConsecutiveOnes(nums):
    res = cnt = 0

    for n in nums:
        if n == 1:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    
    return max(res, cnt)



def maxConsecutiveOnesII(nums):
    res = cnt = 0

    for n in nums:
        if n == 1:
            cnt += 1
            if cnt > res:
                res = cnt
        else:
            cnt = 0
    
    return res


nums = [1,1,0,1,1,1]
output = 3

mc = maxConsecutiveOnes(nums)
mc2 = maxConsecutiveOnesII(nums)

print('With max', mc)
print('Without max', mc2)
print(output)