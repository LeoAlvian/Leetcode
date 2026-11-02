"""
698. Partition to K Equal Sum Subsets

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.



Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""



def canPartitionKSubsets(nums, k):
    if sum(nums) % k:
        return False
    nums.sort(reverse=True)

    target = sum(nums) // k
    used = [False] * len(nums)

    def backtrack(i, k, subsetSum):
        if k == 0:
            return True
        # If subsetSum == target, recurse to build the next subset
        if subsetSum == target:
            return backtrack(0, k - 1, 0)
        
        # For each unused element from index i:
        #     Skip if adding it exceeds the target.
        #     Mark as used and recurse.
        #     Backtrack by unmarking.
        #     Pruning: If subsetSum == 0 and we failed, return false immediately.
        for j in range(i, len(nums)):
            if used[j] or subsetSum + nums[j] > target:
                continue

            used[j] = True
            if backtrack(j + 1, k, subsetSum + nums[j]):
                return True
            used[j] = False


            # If we fail to place any element into an empty subset (when subsetSum == 0), 
            # we know that element cannot be placed anywhere, so the entire configuration 
            # is invalid. This avoids redundant exploration of branches that will never 
            # succeed.
            if subsetSum == 0:
                return False

        return False

    return backtrack(0, k, 0)



nums = [4,3,2,3,5,2,1]
k = 4
output = True

res = canPartitionKSubsets(nums, k)

print(res)
print(output)