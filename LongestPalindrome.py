"""
409. Longest Palindrome

Solved
Easy
Topics
premium lock icon
Companies

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.



Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

from collections import defaultdict
# Use Hash Map 
def longestPalindrome(s):
    count = defaultdict(int)
    res = 0

    for c in s:
        count[c] += 1
        if count[c] % 2 == 0:
            res += 2
    
    for cnt in count.values():
        if cnt % 2:
            res += 1
            break

    return res


# Using Hash Set
def longestPalindromeSet(s):
    seen = set()
    res = 0

    for c in s:
        if c in seen:
            seen.remove(c)
            res += 2
        else:
            seen.add(c)

    return res + 1 if seen else res



s = "abccccdd"
output = 7

res = longestPalindrome(s)
res2 = longestPalindromeSet(s)

print(res)
print(res2)
print(output)