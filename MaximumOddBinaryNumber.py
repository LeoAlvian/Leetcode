"""
2864. Maximum Odd Binary Number

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".



Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
 

Constraints:

1 <= s.length <= 100
s consists only of '0' and '1'.
s contains at least one '1'.
"""



# Using Two pointer technique with time: O(n) and space: O(n)

def maximumOddBinaryNumber(s):
    ls = [c for c in s] # change string of s into a list because string are immutable
    l = 0               # a left pointer

    for i in range(len(ls)):
        if ls[i] == '1':
            ls[i], ls[l] = ls[l], ls[i]
            l += 1
    
    ls[l - 1], ls[len(s) - 1] = ls[len(s) - 1], ls[l - 1]

    return ''.join(ls)


# Using Greedy Approach, we count every '1' and just subtract one to be placed in the right 
# most side of the string and the rest gonna be the right most side and the fill the middle 
# with '0'
# Also this solution is slightly faster on leetcode

def maximumOddBinaryNumberII(s):
    count = 0  # Count every one on the string s

    for c in s:
        if c == '1':
            count += 1
    
    return '1' * (count - 1) + '0' * (len(s) - count) +'1'


s = "0101"
output = "1001"

res = maximumOddBinaryNumber(s)
res2 = maximumOddBinaryNumberII(s)

print(res)
print(res2)
print(output)