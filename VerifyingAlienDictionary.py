"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.



Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.



Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

def verifyAlienDictionay(words, order):
    # Map character to it's index in sequence of order
    # Ex :
    # order = "hla" 
    # orderIdx = {h:0, l:1, a:2}
    # then we loop through each words and compare them and then check each character
    # if len(w1) > len(w2) return False
    # if w1[j] != w2[j]
    # if orderIdx[w2] < orderIdx[w1] return False
    orderIdx = {c:i for i, c in enumerate(order)}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        for j in range(len(w1)):
            if j == len(w2):
                return False
            if w1[j] != w2[j]:
                if orderIdx[w2[j]] < orderIdx[w1[j]]:
                    return False
                break
    
    return True





def isAlienSorted(words, order):
    order_map = {char: i for i, char in enumerate(order)}
    
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        
        for j in range(len(word1)):
            # If we run out of letters in the second word, and the first is longer, it's invalid
            if j == len(word2):
                return False
            
            if word1[j] != word2[j]:
                if order_map[word1[j]] > order_map[word2[j]]:
                    return False
                break
        else:
            # If we finished the loop without breaking, word1 is a prefix of word2 (e.g., "apple" and "app")
            if len(word1) > len(word2):
                return False
                
    return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
output = True

res = verifyAlienDictionay(words, order)
res2 = isAlienSorted(words, order)

print(res)
print(res2)
print(output)