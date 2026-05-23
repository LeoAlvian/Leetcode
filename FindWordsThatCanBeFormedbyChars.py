"""
1160. Find Words That Can Be Formed by Characters

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.



Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""

from collections import Counter, defaultdict

def countCharacters(words, chars):
    count = Counter(chars)
    res = 0

    for word in words:
        char_count = defaultdict(int)
        good = True
        for char in word:
            char_count[char] += 1
            if char not in count or char_count[char] > count[char]:
                good = False
                break
        if good:
            res += len(word)
    
    return res


words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
output = 10

res = countCharacters(words, chars)

print(res)
print(output)