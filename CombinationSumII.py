"""
40. Combination Sum II

Solved
Medium
Topics
premium lock icon
Companies

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]


Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""



def combinationSum2(cand, t):
    res = []
    cand.sort()

    def dfs(i, cur, total):
        if total == t:
            res.append(cur.copy())
            return
        if total > t or i >= len(cand):
            return

        # Include the current candidate
        cur.append(cand[i])
        dfs(i + 1, cur, total + cand[i])

        # Not include the current candidate but also remember that if we skip this current candidate, we want to skip all the same current candidate in the arr
        cur.pop()
        while i + 1 < len(cand) and cand[i] == cand[i + 1]:
            i += 1
        dfs(i + 1, cur, total)


    dfs(0, [], 0)
    return res


candidates = [10,1,2,7,6,1,5]
target = 8
output = [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

res = combinationSum2(candidates, target)

print(res)
print(output)