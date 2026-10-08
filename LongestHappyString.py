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





def longestHappyStrII(a, b ,c):
    curra, currb, currc = 0, 0, 0
    # Maximum total iterations possible is given by the sum of a, b, and c.
    total_iterations = a + b + c
    result = []

    for i in range(total_iterations):
        if (a >= b and a >= c and curra != 2) or (
            a > 0 and (currb == 2 or currc == 2)
        ):
            # If 'a' is maximum and its streak is less than 2, or if streak of 'b' or 'c' is 2, then 'a' will be the next character.
            result.append("a")
            a -= 1
            curra += 1
            currb = 0
            currc = 0
        elif (b >= a and b >= c and currb != 2) or (
            b > 0 and (currc == 2 or curra == 2)
        ):
            # If 'b' is maximum and its streak is less than 2, or if streak of 'a' or 'c' is 2, then 'b' will be the next character.
            result.append("b")
            b -= 1
            currb += 1
            curra = 0
            currc = 0
        elif (c >= a and c >= b and currc != 2) or (
            c > 0 and (curra == 2 or currb == 2)
        ):
            # If 'c' is maximum and its streak is less than 2, or if streak of 'a' or 'b' is 2, then 'c' will be the next character.
            result.append("c")
            c -= 1
            currc += 1
            curra = 0
            currb = 0

    return "".join(result)





a = 1
b = 1
c = 7
output = "ccaccbcc"

lhs = longestHappyStr(a, b, c)
lhs2 = longestHappyStrII(a, b, c)

print(lhs)
print(lhs2)
print(output)