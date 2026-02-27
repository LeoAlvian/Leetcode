"""
28. Find the Index of the First Occurrence in a String

Solved
Easy
Topics
premium lock icon
Companies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.



Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Example 3:
haystack = "neevcodeneetcode", needle = "neet"
output = 8
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


# Knuth-Morris-Pratt (KMP) Algorithm and using LPS(Longest Prefix Suffix) array
# Time complexity O(m + n) and O(n) space

def strStr(haystack, needle):
    if needle == '': return -1
    n = len(needle)
    lps = [0] * n

    prevLps, i = 0, 1
    while i < n:
        if needle[i] == needle[prevLps]:
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        elif prevLps == 0:
            lps[i] = 0
            i += 1
        else:
            prevLps = lps[prevLps - 1]

    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == n:
            return i - n
    
    return -1



# Using built-in function find with faster time in leetcode
def strStrII(haystack, needle):
    return haystack.find(needle)
    

haystack = "neevcodeneetcode"
needle = "neet"
output = 8

print(strStr(haystack, needle))
print(strStrII(haystack, needle))
print(output)