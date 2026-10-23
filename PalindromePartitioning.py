"""
131. Palindrome Partitioning

Solved
Medium
Topics
premium lock icon
Companies

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]



Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""


# Solving it using backtrack or dfs with time: O(n * 2^n) space: O(n) extra and 
# O(n * 2^n) for the output

def partition(s):
    res = []
    part = []

    def isPalin(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if isPalin(s, i, j):
                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res



s = "aab"
output = [["a","a","b"],["aa","b"]]

res = partition(s)

print(res)
print(output)