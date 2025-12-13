"""
Docstring for WordBreakII

140. Word Break II

Solved
Hard
Topics
premium lock icon
Companies

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]


Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.


Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""

# Using backtrack to solve this solution

def wordBreakII(s, wordDict):
    wd = set(wordDict)
    cache = {}

    def backtrack(i):
        if i == len(s):
            return ['']
        if i in cache:
            return cache[i]

        res = []
        for j in range(i, len(s)):
            w = s[i:j+1]
            if w not in wd:
                continue

            strings = backtrack(j + 1)
            if not strings:
                continue
            for substr in strings:
                sentence = w
                if substr:
                    sentence += ' ' + substr
                res.append(sentence)
        
        cache[i] = res
        return res
    
    return backtrack(0)

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
output = ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

wb = wordBreakII(s, wordDict)
print(wb)
print(output)