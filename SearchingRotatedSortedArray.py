"""
81. Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true



Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""


# Use nested Binary search algorithm

# we gonna search using normal binary search with a catch, which is if the middle 
# part is bigger which means we are on the left side of the arr but if middle 
# is smaller we are in the right side, but also if middle are equal which means 
# there is duplicate and we need to keep inrement l until it is not equal
# When we are on the left side we need to check if nums[l] <= target < nums[mid] 
# if yes we need to change r = mid - 1 else change l = mid + 1
# But if we are on the right side of the arr and nums[mid] < target <= nums[r],
# change l = mid + 1 else change r = mid - 1
#
# Ex
# nums = [2,5,6,0,0,1,2], target = 0
#
# nums = [2,5,6,0,0,1,2]  -> nums[m] == 0
#         l   m       r   -> nums[l] < nums[m]
#                            if nums[l] <= target < nums[m]
#                            2 <= 0 < 6, NO l = mid + 1       
# nums = [2,5,6,0,0,1,2]  -> nums[m] == 0, yes then return True
#               l m   r

def searchRotatedSortedArray(nums, target):
    # There is faster way but we used set and this is not recomended for interview
    # return True if target in Set(nums) else False
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return True
        
        if nums[l] < nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[l] > nums[m]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            l += 1
    
    return False

nums = [2,5,6,0,0,1,2]
target = 0
output = True
srs = searchRotatedSortedArray(nums, target)
print(srs)
print(output)