"""
Docstring for PermutationsII

47. Permutations II

Solved
Medium
Topics
premium lock icon
Companies

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

# Using backtrack to solve this problem

def permutationII(nums):
    res = []
    perm = []
    count = { n:0 for n in nums }
    for n in nums:
        count[n] += 1
    
    def backtrack():
        if len(perm) == len(nums):
            res.append(perm.copy())
            return

        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                backtrack()
                
                # Cleanup for recursive function
                count[n] += 1
                perm.pop()
    
    backtrack()
    return res


nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

p = permutationII(nums)
print(p)
print(output)