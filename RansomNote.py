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

    for c in ranCount:
        if ranCount[c] > magCount[c]:
            return False
    return True



ransomNote = "aab"
magazine = "aaab"
output = True

cc = canConstruct(ransomNote, magazine)

print(cc)
print(output)