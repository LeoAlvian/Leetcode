"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.


Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]


Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""


# Modify the original arr and adding second param x for how many times wew gonna 
# concatenate the arr
def getConcatenatedX(nums, x):
    leng = len(nums)

    for i in range(x - 1):
        for n in range(leng):
            nums.append(nums[n])
    
    return nums


def getConcatenated(nums):
    ans = []

    for i in range(2):
        for n in range(len(nums)):
            ans.append(nums[n])
    
    return ans


x = 3
nums = [1,3,2,1]
output = [1,3,2,1,1,3,2,1]
gc = getConcatenated(nums)
print(gc)
print(gc == output)
gcx = getConcatenatedX(nums, x)
print(gcx)
print(gcx == output)