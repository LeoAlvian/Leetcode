"""
680. Valid Palindrome II - Explanation

Description
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).


Example 1:

Input: s = "aca"
Output: true
Explanation: "aca" is already a palindrome.


Example 2:

Input: s = "abbadc"
Output: false
Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.


Example 3:

Input: s = "abbda"
Output: true
Explanation: "We can delete the character 'd'.

Constraints:

1 <= s.length <= 100,000
s is made up of only lowercase English letters.
"""


def palindromeII(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            skipL, skipR = s[l + 1: r + 1], s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]

        l, r = l + 1, r - 1
    
    return True


s = "abbda"
output = True
p2 = palindromeII(s)
print(p2)
print(output)