"""
Docstring for FindAllNumbersDisappearedinArr

448. Find All Numbers Disappeared in an Array

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]



Example 2:
Input: nums = [1,1]
Output: [2]


Example 3:
Input: nums = [1,4,1,4,4]
Output: [2,3,5]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""



def numDissapearedinArr(nums):
    n = len(nums) + 1
    seen = [False] * n
    # print('seen before =',seen)
    # index      =        [   1,     2,     3,     4,     5  ]
    # nums       =        [   1,     4,     1,     4,     4  ]
    # seen before = [False, False, False, False, False, False]

    for i in nums:
        seen[i] = True
    # print('seen after =',seen)
    # index      =       [   1,     2,    3,     4,    5  ]
    # nums       =       [   1,     4,    1,     4,    4  ]
    # seen after = [False, True, False, False, True, False]
    
    return [i for i in range(1, n) if not seen[i]]


nums = [1,4,1,4,4]
output = [2,3,5]

nda = numDissapearedinArr(nums)

print(nda)
print(output)