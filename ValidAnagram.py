"""
242. Valid Anagram

Description
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


Example 1:

Input: s = "racecar", t = "carrace"
Output: true


Example 2:

Input: s = "jar", t = "jam"
Output: false


Constraints:

s and t consist of lowercase English letters.
"""

# We use hashMap and map how many occurance of each character in string s and
# string t and then if all the count match that means we have a valid anagram
# Ex
# s = "racecar"
# t = "carrace"
#
#        s                    t
# _________________   _________________
# | char  | count |   | char  | count |
# |---------------|   |---------------|
# |   r   |   2   |   |   r   |   2   |
# |   a   |   2   |   |   a   |   2   |
# |   c   |   2   |   |   c   |   2   |
# |   e   |   1   |   |   e   |   1   |
# |---------------|   |---------------|
def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

def validAnagramSort(s, t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


s = "racecar"
t = "carrace"
output = True
va = validAnagram(s, t)
print(va)
print(output)
vas = validAnagramSort(s, t)
print('sort', vas)