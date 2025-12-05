"""
1405. Longest Happy String

Solved
Medium
Topics
premium lock icon
Companies
Hint

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 
Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.


Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

# This problem is similar to ReorganizeString.py but with some twist that we are 
# allowed to have maximum 2 consicutive/substring of the same character before we add 
# another charachter, so by checking if res[-2] == res[-1] == char we can check if the 
# previous two character are the same, if it is we gonna pop another one from the heap 
# and then add that char to res and add both to the heap

import heapq

def longestHappyStr(a, b, c):
    res, maxHeap = '', []
    for count, char in [(-a, 'a'), (-b, 'b'),(-c, 'c')]:
        if count:
            heapq.heappush(maxHeap, (count,char))
    
    while maxHeap:
        count, char = heapq.heappop(maxHeap)
        if len(res) > 1 and res[-2] == res[-1] == char:
            if not maxHeap:
                break
            count2, char2 = heapq.heappop(maxHeap)
            res += char2
            count2 += 1
            if count2:
                heapq.heappush(maxHeap, (count2, char2))
        else:
            res += char
            count += 1
        if count:
            heapq.heappush(maxHeap, (count, char))
    
    return res

a = 1
b = 1
c = 7
output = "ccaccbcc"
lhs = longestHappyStr(a, b, c)
print(lhs)
print(output)