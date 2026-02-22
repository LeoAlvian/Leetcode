"""
387. First Unique Character in a String

Solved
Easy
Topics
premium lock icon
Companies

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.



Example 2:
Input: s = "loveleetcode"
Output: 2



Example 3:
Input: s = "aabb"
Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

# Using defaultdict to count how many char appear in s

from collections import defaultdict

def firstUniqChar(s):
    count = defaultdict(int)

    for c in s:
        count[c] += 1
    # defaultdict(<class 'int'>,{'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1})
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1


# Using Counter to count how many char appear in s, and this is faster on leetcode
from collections import Counter

def firstUniqCharII(s):
    count = Counter(s)
    # Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1


s = "loveleetcode"
output = 2 

print(firstUniqChar(s))
print(firstUniqCharII(s))
print(output)