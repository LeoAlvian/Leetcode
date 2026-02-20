"""
Docstring for RansomNote

383. Ransom Note

Solved
Easy
Topics
premium lock icon
Companies

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false



Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false



Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# Using Two Hash Map and built in Counter method, and compare if the count of char in 
# ransomNote <= count char in magazine, if it is not then return False

from collections import Counter

def canConstruct(ransomNote, magazine):
    ranCount = Counter(ransomNote)
    magCount = Counter(magazine)

    for char, cnt in ranCount.items():
        if char not in magCount:
            return False
        elif magCount[char] < cnt:
            return False
    return True


# Using set and count method for string in python
def canConstructII(ransomNote, magazine):
    for c in set(ransomNote):
        if magazine.count(c) < ransomNote.count(c):
            return False
    return True



ransomNote = "aab"
magazine = "aabb"
output = True

cc = canConstruct(ransomNote, magazine)
cc2 = canConstructII(ransomNote, magazine)

print(cc)
print(cc2)
print(output)