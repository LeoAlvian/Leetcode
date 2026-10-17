"""
46. Permutations

Solved
Medium
Topics
premium lock icon
Companies

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]




Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""



# Solving using backtrack with time: O(n * n!) and space: O(n)

def permute(nums):
    if len(nums) == 0:
        return [[]]

    perms = permute(nums[1:])
    res = []


    for p in perms:
        for i in range(len(p) + 1):
            temp = p.copy()
            temp.insert(i, nums[0])
            res.append(temp)

    # p: [], nums[0]: 3, temp: [3]
    # p: [3], nums[0]: 2, temp: [2, 3]
    # p: [3], nums[0]: 2, temp: [3, 2]
    # p: [2, 3], nums[0]: 1, temp: [1, 2, 3]
    # p: [2, 3], nums[0]: 1, temp: [2, 1, 3]
    # p: [2, 3], nums[0]: 1, temp: [2, 3, 1]
    # p: [3, 2], nums[0]: 1, temp: [1, 3, 2]
    # p: [3, 2], nums[0]: 1, temp: [3, 1, 2]
    # p: [3, 2], nums[0]: 1, temp: [3, 2, 1]
    
    return res


nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

res = permute(nums)

print(res)
print(output)