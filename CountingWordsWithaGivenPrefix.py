"""
2185. Counting Words With a Given Prefix

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".



Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.count += 1
    
    def countW(self, pref):
        cur = self.root

        for char in pref:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        
        return cur.count

class Solution:
    def prefixCountII(self, words, pref):
        prefix_tree = PrefixTree()

        for word in words:
            if len(word) >= len(pref):
                prefix_tree.add(word)
        return prefix_tree.countW(pref)


# Time complexity is O(m * n) Where m is the number of words and n is the length of the
# string pref. because we use brute force and space is O(1)
# This is fast for easy problem because the input is small
def prefixCount(words, pref):
    N = len(pref)
    res = 0

    for word in words:
        if word[:N] == pref:
            res += 1

    return res


words = ["pay","attention","practice","attend"]
pref = "at"
output = 2

res = prefixCount(words, pref)

# The solution below is using Prefix Trie with faster time if the input is really large, 
# this is good solution for hard problem
# Time: O(m * l + n)
# Space: O(m * l)
s = Solution()
res2 = s.prefixCountII(words, pref)

print(res)
print(res2)
print(output)