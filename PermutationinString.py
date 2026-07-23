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


# Using Hash Map + Sliding Windows

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



# Using Array + Sliding Windows

def checkInclusionII(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26

    

s1 = "ab"
s2 = "eidbaooo"
output = True

res = checkInclusion(s1, s2)
res2 = checkInclusionII(s1, s2)

print(res)
print(res2)
print(output)