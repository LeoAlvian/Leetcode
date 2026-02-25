"""
791. Custom Sort String

Solved
Medium
Topics
premium lock icon
Companies

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.




Example 2:
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.



Example 3:
order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"

output = "hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"
 

Constraints:

1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
"""


from collections import Counter

def customSortString(order, s):
    count = Counter(s)
    res = []
    # print(count)
    # Counter({'q': 11, 'a': 9, 't': 8, 'z': 5, 'd': 5, 'x': 5, 'h': 5, 'o': 4, 'm': 4, 
    # 'g': 4, 'k': 4, 'l': 4, 'f': 4,'j': 4, 'p': 3, 's': 3, 'c': 3, 'n': 3, 'u': 2, 
    # 'y': 2, 'b': 2, 'i': 2, 'e': 1, 'v': 1, 'w': 1, 'r': 1})
    
    for c in order:
        while count[c]:
            res.append(c)
            count[c] -= 1
    
    for c in count:
        while count[c]:
            res.append(c)
            count[c] -= 1
    
    return ''.join(res)


def customSortStringII(order, s):
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    
    # Map count to it's index with ord(c) - ord('a') => c = b => b - a = 1 so index of 
    # b is 1
    # print(count)
    # [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p,  q, r, s, t, u, p, w, x, y, z]
    # [9, 2, 3, 5, 1, 4, 4, 5, 2, 4, 4, 4, 4, 3, 4, 3, 11, 1, 3, 8, 2, 1, 1, 5, 2, 5]
    
    res = []
    for c in order:
        i = ord(c) - ord('a')
        while count[i]:
            res.append(c)
            count[i] -= 1
    
    for i in range(26):
        char = chr(ord('a') + i)
        while count[i]:
            res.append(char)
            count[i] -= 1
    
    return ''.join(res)



order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"

output = "hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"

# With the first method we didn't preserve the order after we finish with order string
print(customSortString(order, s))
# We preserve the order with second function becuase we use ord() function
print(customSortStringII(order, s))
print(output)