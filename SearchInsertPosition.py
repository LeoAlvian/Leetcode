"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2



Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1



Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104 
"""

# We gonna use Binary search since it require us to have O(log n) time complexity
#
# nums = [1,3,5,6]  , target = 7  , output = 4
#         l m   r     -> we gonna loop while l <= r then calculate middle part
#                     -> since l = 0, r = 3, m = 0 + 3 // 2 
#                     -> check if nums[mid] == target if yes return mid else
#                     -> if nums[mid] < target then l = mid + 1 else r = mid - 1 
#                     -> then return l
def searchInsertPos(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid 
        
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return l

nums = [1,3,5,6]
target = 7
output = 4
sip = searchInsertPos(nums, target)
print(sip)
print(output)