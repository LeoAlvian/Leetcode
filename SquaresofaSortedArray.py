"""
977. Squares of a Sorted Array

Solved
Easy
Topics
premium lock icon
Companies

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].



Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

# using sort algorithm with time complexity of O(n logn)

# def sortedSquaresSort(nums):


# Using two pointer and idx to put value in a correct order so we don't have to reverse 
# it
#
# Ex:
#
# res  = [ 0,  0, 0, 0,  0]
#                        i
# nums = [-7, -3, 2, 3, 11]
#          l            r
# check if abs(l) > abs(r) => 7 > 11 => False
# res[i] = 11 * 11 = 121
# then decrement r and i
#
# res  = [ 0,  0, 0, 0, 121]
#                    i
# nums = [-7, -3, 2, 3, 11]
#          l         r
# check if abs(l) > abs(r) => 7 > 3 => True
# res[i] = 7 * 7 = 49
# then increment l and decrement i
#
# res  = [ 0,  0, 0, 49, 121]
#                 i
# nums = [-7, -3, 2, 3, 11]
#              l     r
# check if abs(l) > abs(r) => 3 > 3 => True
# res[i] = 3 * 3 = 9
# then decrement r and i
#
# res  = [ 0,  0, 9, 49, 121]
#              i
# nums = [-7, -3, 2, 3, 11]
#              l  r
# check if abs(l) > abs(r) => 3 > 2 => False
# res[i] = 3 * 3 = 9
# then increment l and decrement i
#
# res  = [ 0,  9, 9, 49, 121]
#          i
# nums = [-7, -3, 2, 3, 11]
#                lr
# check if abs(l) > abs(r) => 2 > 2 => False
# res[i] = 2 * 2 = 4
# then increment l and decrement i
#
# res  = [ 4,  9, 9, 49, 121]
#          i
# nums = [-7, -3, 2, 3, 11]
#                 r  l
# because l pass r we exit the loop and return res


def sortedSquares(nums):
    n = len(nums)
    res = [0] * n
    print(res)
    l, r = 0, n - 1
    idx = n - 1

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[idx] = nums[l] * nums[l]
            l += 1
        else:
            res[idx] = nums[r] * nums[r]
            r -= 1
        idx -= 1
    print(res)
    return res


nums = [-7,-3,2,3,11]
output = [4,9,9,49,121]


print(sortedSquares(nums))
print(output)