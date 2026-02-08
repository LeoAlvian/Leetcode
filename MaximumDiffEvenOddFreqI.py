"""
Docstring for Maximum Difference Between Even and Odd Frequency I

3442. Maximum Difference Between Even and Odd Frequency I

Easy
Topics
premium lock icon
Companies
Hint

You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:
Input: s = "aaaaabbc"
Output: 3
Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.



Example 2:
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
"""

# This function is slower on leetcode even though the time complexity is O(n)
from collections import Counter

def maxDiffEvenOddFreqICounter(s):
    count = Counter(s)
    oddMax = 0
    evenMin = len(s)

    for cnt in count.values():
        if cnt & 1:
            oddMax = max(oddMax, cnt)
        else:
            evenMin = min(evenMin, cnt)
    
    return oddMax - evenMin


# This function is faster on leetcode even thought the time complexity is O(n)
def maxDiffEvenOddFreqI(s):
    charCount = {}
    for c in s:
        charCount[c] = charCount.get(c, 0) + 1
    
    oddMax = 0
    evenMin = len(s)

    for c in s:
        freq = charCount[c]
        if freq & 1:
            oddMax = max(oddMax, freq)
        else:
            evenMin = min(evenMin, freq)
    
    return oddMax - evenMin



s = "aaaaabbc"
output = 3 

md = maxDiffEvenOddFreqI(s)

print(md)
print(output)