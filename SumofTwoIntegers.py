"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.


Example 1:
Input: a = 1, b = 2
Output: 3


Example 2:
Input: a = 2, b = 3
Output: 5
 
Constraints:

-1000 <= a, b <= 1000
"""


def getSum(a, b):
    mask = 0xFFFFFFFF
    maxInt = 2**31 - 1

    while b != 0:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = carry << 1
    
    return a if a <= maxInt else ~(a ^ mask)




a = -2
b = 3
output = 5
res = getSum(a, b)
print('result', res)