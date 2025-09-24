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

# def hammingWeight(n):
#     res = 0

#     while n:
#         res += n % 2
#         n = n >> 1
    
#     return res



# This function is a bit better because we don't have to loop through all the zero bit
# We just add 1 to result if the bit is one else we skip it
# By using n = n & n - 1 we just skip all zero
# Example
# n, res = 1001, 0
# n - 1 => 1001 - 1 => 1000
# n & n - 1 => 1001 & 1000 => 1000
# res == 1
# n - 1 => 1000 - 1 => 0111
# n & n - 1 => 1000 & 0111 => 0000
# res == 2
# end loop because n = 0000 now so we only loop as many as 1 in the bit

def hammingWeight(n):
    res = 0

    while n:
        n &= n - 1
        res += 1
    
    return res


res = hammingWeight(n)
print('res',res)
print(output == res)