"""
205. Isomorphic Strings

Solved
Easy
Topics
premium lock icon
Companies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.



Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.



Example 3:
Input: s = "paper", t = "title"
Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


# Using two map to map string s to string t and string t to string s
# if we find a character that is map to the same character in other string then
# we return false immedietely
def isomorphicStrings(s, t):
    mapST, mapTS = {}, {}

    for c1, c2 in zip(s, t):
        if c1 in mapST and mapST[c1] != c2 or c2 in mapTS and mapTS[c2] != c1:
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    
    return True



s = "paper"
t = "title"
output = True

iss = isomorphicStrings(s, t)

print(iss)
print(output)