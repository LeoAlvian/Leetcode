"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.



Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1



Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

# Using sliding windows algorithm to solve this problem
# Ex
# target = 7
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 0 + 2 = 2 
#         lr                  -> if total >= target we remove nums[l] and increment l
#                             -> else increment r
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 2 + 3 = 5 
#         l  r 
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 5 + 1 = 6
#         l     r
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 6 + 2 = 8 
#         l        r          -> now total >= target remove nums[l] from total and 
#                             -> increment l so total = 8 - 2 = 6
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 6 + 4 = 10 
#            l        r       -> now total >= target remove nums[l] from total and 
#                             -> increment l so total = 10 - 3 = 7
# nums = [2, 3, 1, 2, 4, 3]   -> add nums[r] to total -> total = 7 + 3 = 10 
#               l        r    -> now total >= target remove nums[l] from total and 
#                             -> increment l so total = 10 - 1 = 9
# nums = [2, 3, 1, 2, 4, 3] 
#                     l  r    -> now total >= target remove nums[l] from total and 
#                             -> increment l so total = 9 - 2 = 7


def minSizeSubSum(nums, target):
    l, total = 0, 0
    res = float('inf')

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1
    
    return 0 if res == float('inf') else res


target = 7
nums = [2,3,1,2,4,3]
output = 2
mss = minSizeSubSum(nums, target)
print(mss)
print(output)