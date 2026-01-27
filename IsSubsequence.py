"""
Docstring for IsSubsequence

392. Is Subsequence

Description
You are given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:
Input: s = "node", t = "neetcode"
Output: true



Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false



Constraints:

0 <= s.length <= 100
0 <= t.length <= 10,000
s and t consist only of lowercase English letters.
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 1,000,000,000, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""



def isSubsequence(s, t):
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)


s = "node"
t = "neetcode"
output = True

iss = isSubsequence(s, t)

print(iss)
print(output)