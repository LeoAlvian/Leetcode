"""
Docstring for JumpGameVII

1871. Jump Game VII

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.



Example 2:
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""

from collections import deque

def jumpGameVII(s, minJump, maxJump):
    n = len(s) - 1
    if s[-1] == '1':
        return False
    elif minJump == maxJump:
        return n * minJump == 0 and all(c == '0' for c in s[minJump:n:minJump])
    elif minJump == 1:
        return '1' * maxJump not in s
    
    q, farthest = deque([0]), 0

    while q:
        i = q.popleft()
        start = max(i + minJump, farthest + 1)
        for j in range(start, min(i + maxJump + 1, len(s))):
            if s[j] == '0':
                if j == len(s) - 1:
                    return True
                q.append(j)
        farthest = i + maxJump
    
    return False



s = "011010"
minJump = 2
maxJump = 3
output = True

jg = jumpGameVII(s, minJump, maxJump)
print(jg)
print(output)