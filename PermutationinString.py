"""
567. Permutation in String

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").



Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


def checkInclusion(s1, s2):
    s1Hash = {}
    s2Hash = {}
    l = 0

    for c in s1:
        s1Hash[c] = 1 + s1Hash.get(c, 0)

    for r in range(len(s2)):
        if r - l + 1 > len(s1):
            s2Hash[s2[l]] -= 1
            if s2Hash[s2[l]] == 0:
                s2Hash.pop(s2[l])
            l += 1

        s2Hash[s2[r]] = 1 + s2Hash.get(s2[r], 0)

        if s1Hash == s2Hash:
            return True
    return False

    

s1 = "ab"
s2 = "eidbaooo"
output = True

res = checkInclusion(s1, s2)

print(res)
print(output)