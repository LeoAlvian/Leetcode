"""
1624. Largest Substring Between Two Equal Characters

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.



Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".



Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.



Example 4:

Input: s = "abhdfcabzxya"
Output: 10
Explanation: There are a in the beginning and the last.
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""


def maxLengthBetweenEqualCharacters(s):
    char_idx = {} # map first character appear to their index
    res = -1

    for i, c in enumerate(s):
        if c in char_idx:
            res = max(res, i - char_idx[c] - 1)
        else:
            char_idx[c] = i

    return res


s = "abhdfcabzxya"
output = 10

res = maxLengthBetweenEqualCharacters(s)

print(res)
print(output)