"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321


Example 2:
Input: x = -123
Output: -321


Example 3:
Input: x = 120
Output: 21
"""

import math

def reverInt(x):
    Max = 2**31 - 1
    Min = -2**31

    res = 0
    while x:
        digit = int(math.fmod(x, 10))
        x = int(x // 10)

        if res > Max // 10 or (res == Max // 10 and digit >= Max % 10):
            return 0
        if res < Min // 10 or (res == Min // 10 and digit <= Min % 10):
            return 0
        
        res = (res * 10) + digit
    
    return res




x = 120
output = 21
ri = reverInt(x)
print(ri)