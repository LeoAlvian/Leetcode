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

# Intuition
# Numbers can only conflict if their difference is exactly k. This means numbers that differ by k form chains where adjacent elements cannot both appear in a beautiful subset. By grouping numbers into these chains, we transform the problem into independent subproblems.

# For each chain, we solve a variation of the house robber problem: at each position, we either skip the current number or include some combination of its duplicates (if the number appears multiple times). If we include any copies of a number, we must skip the next number in the chain.

# Algorithm
#   1. Count the frequency of each number using a hash map.
#   2. Build groups where each group contains numbers that form a chain differing by k (e.g., [1, 3, 5] for k=2).
#   3. For each group, use memoized recursion starting from the smallest number.
#   4. At each number n in a group, either skip it (recurse to n + k) or include some of its copies and skip the next (recurse to n + 2k).
#   5. When including a number with count c, there are 2^c - 1 ways to choose which copies to include.
#   6. Multiply the results from all independent groups and subtract 1 for the empty subset.

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
        # skip the current number
        skip = helper(n + k, g)
        # include the current number
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