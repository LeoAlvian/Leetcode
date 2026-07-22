"""
424. Longest Repeating Character Replacement

Solved
Medium
Topics
premium lock icon
Companies

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.



Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


# Using sliding windows and Hash Map to map every character to its count

# We gonna count every occurences of char in s
# then while range of windows which we can get it from (r - l + 1) - max count > k,
# we decrease the window

# Time: O(m * n) and space: O(m)

# Ex: 
# s = "AABABBA", k = 1
# res = max(res, r - l + 1)

# AABABBA
# |
# count = {'A': 1}              res = 1, l = 0, r = 0

# AABABBA
#  |
# count = {'A': 2}              res = 2, l = 0, r = 1

# AABABBA
#   |
# count = {'A': 2, 'B': 1}      res = 3, l = 0, r = 2

# AABABBA
#    |
# count = {'A': 3, 'B': 1}      res = 4, l = 0, r = 3

# AABABBA
#     |
# count = {'A': 3, 'B': 2}      res = 4, l = 0, r = 4

# AABABBA
#     |
# count = {'A': 1, 'B': 2}      res = 4, l = 2, r = 4

# AABABBA
#      |
# count = {'A': 1, 'B': 3}      res = 4, l = 2, r = 5

# AABABBA
#       |
# count = {'A': 2, 'B': 3}      res = 4, l = 3, r = 6

def characterReplacement(s, k):
    count = {}
    res, l = 0, 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    
    return res



# Optimize with time: O(n) and space: O(m)

def characterReplacementII(s, k):
    count = {}
    res, l = 0, 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    
    return res


s = "AABABBA"
k = 1
output = 4

res = characterReplacement(s, k)
res2 = characterReplacementII(s, k)

print(res)
print(res2)
print(output)