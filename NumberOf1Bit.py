"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 
Example 1:
Input: n = 11
Output: 3

Explanation:
The input binary string 1011 has a total of three set bits.


Example 2:
Input: n = 128
Output: 1

Explanation:
The input binary string 10000000 has a total of one set bit.


Example 3:
Input: n = 2147483645
Output: 30

Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
"""


n = 2147483645
output = 30


# This work by shifting incrementing res by 1 after we mod n by 2 because we just get
# the reminder of it and then we shift the bits by one and continue looping
# But this process we gonna loop through all bits even if it 0
def hammingWeight(n):
    res = 0

    while n:
        res += n % 2
        n = n >> 1
    
    return res


res = hammingWeight(n)
print('res',res)
print(output == res)