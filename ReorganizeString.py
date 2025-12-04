"""
767. Reorganize String

Solved
Medium
Topics
premium lock icon
Companies
Hint


You are given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

You can return any possible rearrangement of s or return "" if not posssible.

Example 1:
Input: s = "axyy"
Output: "xyay"


Example 2:
Input: s = "abbccdd"
Output: "abcdbcd"


Example 3:
Input: s = "ccccd"
Output: ""


Constraints:

1 <= s.length <= 500.
s is made up of lowercase English characters.
"""

from collections import Counter
import heapq

def reorganizeStr(s):
    count = Counter(s)
    print(count)
    maxHeap = [ [-cnt, char] for char, cnt in count.items() ]
    heapq.heapify(maxHeap)
    print(maxHeap)

    res = ''
    onHoldChar = None

    while maxHeap:
        cnt, char = heapq.heappop(maxHeap)
        res += char
        cnt += 1

        if onHoldChar:
            heapq.heappush(maxHeap, onHoldChar)
            onHoldChar = None
        onHoldChar = [cnt, char] if cnt != 0 else None
    
    return res if not onHoldChar else ''

s = "abbccdd"
output = "abcdbcd"
rs = reorganizeStr(s)
print(rs)
print(output)