"""
2597. The Number of Beautiful Subsets

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].




Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 18
1 <= nums[i], k <= 1000
"""


from collections import Counter

def beautifulSubsets(nums, k):
    cnt = Counter(nums)
    group = []
    visit = set()
    cache = {}

    def helper(n, g):
        if n not in g:
            return 1
        if n in cache:
            return cache[n]
        skip = helper(n + k, g)
        include = (2**g[n] - 1) * helper(n + 2 * k, g)
        cache[n] = skip + include
        return cache[n]

    for n in cnt.keys():
        if n in visit:
            continue
        g = {}
        while n - k in cnt:
            n -= k
        while n in cnt:
            g[n] = cnt[n]
            visit.add(n)
            n += k
        group.append(g)

    res = 1
    for g in group:
        n = min(g.keys())
        res *= helper(n, g)

    return res - 1


nums = [2,4,6]
k = 2
output = 4 

res = beautifulSubsets(nums, k)

print(res)
print(output)