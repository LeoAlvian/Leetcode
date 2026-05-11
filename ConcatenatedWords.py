"""
472. Concatenated Words

Solved
Hard
Topics
premium lock icon
Companies

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".




Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105
"""




def findAllConcatenatedWordsInADict(words):
    wordSet = set(words)
    dp = {}

    def dfs(word):
        if word in dp:
            return dp[word]
        
        for i in range(1, len(word)):
            preffix = word[:i]
            suffix = word[i:]
            if (preffix in wordSet and suffix in wordSet) or (preffix in wordSet and dfs(suffix)):
                dp[word] = True
                return True
        
        dp[word] = False
        return False
        
    
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    
    return res



words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
output = ["catsdogcats","dogcatsdog","ratcatdogcat"]

res = findAllConcatenatedWordsInADict(words)

print(res)
print(output)