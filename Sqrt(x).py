"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.


Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""


# Binary search with time: O(logn) and space: O(1)

def sqrtx(x):
    l, r = 0, x
    res = 0

    while l <= r:
        mid = l + (r - l) // 2
        target = mid * mid
        if target > x:
            r = mid - 1
        elif target < x:
            l = mid + 1
            res = mid
        else:
            return mid
    
    return res


# Using Recursion with time: O(logn) and space: O(logn)

def mySqrtII(x):
    if x < 2:
        return x

    l = mySqrtII(x >> 2) << 1
    r = l + 1
    return l if r ** 2 > x else r


x = 8
output = 2

s = sqrtx(x)
s2 = mySqrtII(x)

print(s)
print(s2)
print(output)