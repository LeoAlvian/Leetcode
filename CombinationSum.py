"""
39. Combination Sum

Solved
Medium
Topics
premium lock icon
Companies

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.




Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""



def combinationSum(cand, t):
    res = []

    def dfs(start, remain, path):
        # Target reached
        if remain == 0:
            res.append(path[:])
            return

        # Try all candidates from start
        for i in range(start, len(cand)):

            # If candidate is too large, skip it
            if cand[i] > remain:
                continue

            # Choose the candidate
            path.append(cand[i])

            # Use the same candidate again
            dfs(i, remain - cand[i], path)

            # Backtrack
            path.pop()

    # Sorting helps us stop early
    cand.sort()
    # Calling the recursive function
    dfs(0, t, [])

    return res


candidates = [2,3,5]
target = 8
output = [[2,2,2,2],[2,3,3],[3,5]]

res = combinationSum(candidates, target)

print(res)
print(output)