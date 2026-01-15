"""
Docstring for GCDTraversal

2709. Greatest Common Divisor Traversal

Solved
Hard
Topics
premium lock icon
Companies
Hint

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

Example 1:
Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.




Example 2:
Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.




Example 3:
Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

# Solve it Using Sieve of Eratosthenes + Disjoint Set Union with time complexity of 
# O(m + n logm) and space of O(n + m) with 352 ms on leetcode

# DSU class
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.par[py] = px
        self.size[px] += self.size[py]
        return True

def gcdTraversal(nums):
    n = len(nums)
    if n == 1:
        return True
    if any(num == 1 for num in nums):
        return False
    
    MAX = max(nums)
    sieve = [0] * (MAX + 1)
    p = 2

    while p * p <= MAX:
        if sieve[p] == 0:
            for composite in range(p * p, MAX + 1, p):
                sieve[composite] = p
        p += 1
    
    uf = UnionFind(n + MAX + 1)
    for i in range(n):
        num = nums[i]
        if sieve[num] == 0: # num is a prime
            uf.union(i, n + num)
            continue

        while num > 1:
            prime = sieve[num] if sieve[num] != 0 else num
            uf.union(i, n + prime)
            while num % prime == 0:
                num //= prime
    
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False
    return True

# Using math.gcd with 20 ms on leetcode
nums = [4,3,12,8]
output = True

gcd = gcdTraversal(nums)

print(gcd)
print(output)