"""
1239. Maximum Length of a Concatenated String with Unique Characters

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.




Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").



Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""


# Solving it using Backtrack with time: O(m * 2^n) and space: O(n) for the recursion stack
# Where n is the number of string and m is the max len of string
from collections import Counter

def maxLength(arr):
    charSet = set()

    def overlap(charS, s):
        c = Counter(charS) + Counter(s)
        # print(c)
        return max(c.values()) > 1

    def backtrack(i):
        if i == len(arr):
            return len(charSet)

        res = 0
        if not overlap(charSet, arr[i]):
            for c in arr[i]:
                charSet.add(c)
            res = backtrack(i + 1)
            for c in arr[i]:
                charSet.remove(c)

        return max(res, backtrack(i + 1))

    return backtrack(0)




# Solving it using BitMask with time: O(n * m) and space: O(n) 
# Where n is the number of string and m is the max len of string 
# way faster time on leetcode

def maxLengthBitMask(arr):
    masks = []
    for w in arr:
        m = 0
        ok = True
        for ch in w:
            b = 1 << (ord(ch) - 97)
            if m & b:
                ok = False
                break
            m |= b
        if ok:
            masks.append(m)
    dp = [0]
    for m in masks:
        for x in dp[:]:
            if not x & m:
                dp.append(x | m)
    return max(bin(x).count('1') for x in dp)






arr = ["cha","r","act","ers"]
output = 6

res = maxLength(arr)
res2 = maxLengthBitMask(arr)

print(res)
print(res2)
print(output)