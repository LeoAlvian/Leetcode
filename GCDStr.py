"""
Docstring for GCDStr

1071. Greatest Common Divisor of Strings

Solved
Easy
Topics
premium lock icon
Companies
Hint

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"



Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"



Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""



Example 4:
Input: str1 = "AAAAAB", str2 = "AAA"
Output: ""



Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

# Using math and iteration with O(min(m, n) * (m + n)) time complexity

def GCDStr(s1, s2):
    len1, len2 = len(s1), len(s2)

    def divisor(l):
        if len1 % l or len2 % l:
            return False
        frac1, frac2 = len1 // l, len2 // l
        return str1[:l] * frac1 == str1 and str1[:l] * frac2 == str2

    for l in range(min(len1, len2), 0, -1):
        if divisor(l):
            return str1[:l]
    
    return ''

import math
# Using math.gcd to find greatest common denominator if we have one and then return that 
# sub string but first we must check if str1 + str2 == str2 + str1, if it is then we can 
# make a sub string from GCD

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    
    g = math.gcd(len(str1), len(str2))
    return str1[:g]


str1 = "ABABAB"
str2 = "ABAB"
output = "AB"

gcds = GCDStr(str1, str2)
gcdo = gcdOfStrings(str1, str2)

print('Iteration', gcds)
print('Math', gcdo)
print(output)