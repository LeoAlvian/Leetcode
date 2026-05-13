"""
516. Longest Palindromic Subsequence

Solved
Medium
Topics
premium lock icon
Companies

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".




Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""



def longestPalindromeSubseq(s):
    return longestCommonSubseq(s, s[::-1])

def longestCommonSubseq(s1, s2):
    N, M = len(s1), len(s2)
    # s = "bbbab"
    dp = [[0] * (M + 1) for i in range(N + 1)]
    # [[0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0]]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    # [[0, 0, 0, 0, 0, 0], 
    #  [0, 1, 1, 1, 1, 1], 
    #  [0, 1, 1, 2, 2, 2], 
    #  [0, 1, 1, 2, 3, 3], 
    #  [0, 1, 2, 2, 3, 3], 
    #  [0, 1, 2, 3, 3, 4]]
    return dp[N][M]


s = "bbbab"
output = 4

res = longestPalindromeSubseq(s)

print(res)
print(output)