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


# We gonna use maxHeap(in python only minHeap but we can get around it by making the 
# value negative) to solve this problem
# First we gonna count how many char appear using Counter method and then put that 
# into a maxHeap, the pop value from maxHeap and add char to result, after that we 
# gonna put that value on hold because we don't want to add the same element twice in 
# a row, after we add another value then we gonna change hold to the new one
#
# Ex:
#
# s = "abbccdd"
# Counter({'b': 2, 'c': 2, 'd': 2, 'a': 1})
# maxHeap = [[-2, 'b'],   -> pop this one and add to res and onHold if cnt != 0
#            [-2, 'c'],      [-2, 'b']
#            [-2, 'd'],      res = 'b', cnt = -1, onHold = [-1, 'b']
#            [-1, 'a']]
#
# maxHeap = [[-2, 'c'],   -> pop this one and add to res and onHold if cnt != 0
#            [-2, 'd'],      [-2, 'c']
#            [-1, 'a'],      res = 'bc', cnt = -1, push onHold, onHold = [-1, 'c']
#            [-1, 'b']]
#
# maxHeap = [[-2, 'd'],   -> pop this one and add to res and onHold if cnt != 0
#            [-1, 'a'],      [-2, 'd']
#            [-1, 'b'],      res = 'bcd', cnt = -1, push onHold, onHold = [-1, 'd']
#            [-1, 'c']]
#
# maxHeap = [[-1, 'a'],   -> pop this one and add to res and onHold if cnt != 0
#            [-1, 'b'],      [-1, 'a']
#            [-1, 'c'],      res = 'bcda', cnt = -1, push onHold, onHold = None
#            [-1, 'd']]
#
# maxHeap = [[-1, 'b'],   -> pop this one and add to res and onHold if cnt != 0
#            [-1, 'c'],      [-1, 'b']
#            [-1, 'd'],      res = 'bcdab', cnt = -1, push onHold, onHold = None
#          
# maxHeap = [[-1, 'c'],   -> pop this one and add to res and onHold if cnt != 0
#            [-1, 'd']]      [-1, 'c']
#                            res = 'bcdabc', cnt = -1, push onHold, onHold = None
#       
# maxHeap = [[-1, 'd']]   -> pop this one and add to res and onHold if cnt != 0
#                            [-1, 'd']
#                            res = 'bcdabcd', cnt = -1, push onHold, onHold = None
# 
# Now maxHeap are [] so we return res if onHold is None else retrun empty string


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