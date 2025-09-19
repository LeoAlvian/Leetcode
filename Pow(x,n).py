"""
Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

You may not use any built-in library functions.


Example 1:

Input: x = 2.00000, n = 5
Output: 32.00000


Example 2:

Input: x = 1.10000, n = 10
Output: 2.59374


Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

x = 1.10000
n = 10
output = 2.59374

def pow(x, n):
    def recursive(x, n):
        if x == 0: return 0
        if n == 0: return 1

        res = recursive(x * x, n // 2)
        return x * res if n % 2 else res

    res = recursive(x, abs(n))
    return res if n >= 0 else 1 / res


res = pow(x, n)
print(res)