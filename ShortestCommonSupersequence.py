"""
1092. Shortest Common Supersequence 

Solved
Hard
Topics
premium lock icon
Companies
Hint

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.



Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""



def shortestCommonSupersequence(str1, str2):
    n, m = len(str1), len(str2)
    prev = [str2[j:] for j in range(m)]
    prev.append('')

    for i in reversed(range(n)):
        cur = [''] * m
        cur.append(str1[i:])

        for j in reversed(range(m)):
            if str1[i] == str2[j]:
                cur[j] = str1[i] + prev[j + 1]
            else:
                res1 = str1[i] + prev[j]
                res2 = str2[j] + cur[j + 1]
                if len(res1) <= len(res2):
                    cur[j] = res1
                else:
                    cur[j] = res2
        prev = cur
    
    return cur[0]



str1 = "abac"
str2 = "cab"
output = "cabac"

res = shortestCommonSupersequence(str1, str2)

print(res)
print(output)