"""
1593. Split a String Into the Max Number of Unique Substrings

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.



Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].



Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
"""




def maxUniqueSplit(s):
    curSet = set()

    def backtrack(start):
        if start == len(s):
            return 0

        res = 0
        for i in range(start, len(s)):
            subStr = s[start:i + 1]
            if subStr in curSet:
                continue
            curSet.add(subStr)
            res = max(res, 1 + backtrack(i + 1))
            curSet.remove(subStr)
        return res

    return backtrack(0)


s = "ababccc"
output = 5 
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].

res = maxUniqueSplit(s)

print(res)
print(output)