"""
Reverse bits of a given 32 bits signed integer.


Example 1:
Input: n = 43261596
Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000


Example 2:
Input: n = 2147483644
Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 

Constraints:

0 <= n <= 231 - 2
n is even.
 

Follow up: If this function is called many times, how would you optimize it?
"""


# Using bit manipulation by formating the input n to a binary 32 bit as a string
# and then reverse it back to integer
# This methods is faster but we didn't learn much about algorithm behind it

# def reverseBits(n):
#     bit = format(n, '032b')
#     return int(bit[::-1], 2)


# This one we trying to manipulate it and understand what's going on under the hud
def reverseBits(n):
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    
    return res


n = 2147483644
output = 1073741822
rb = reverseBits(n)
print(rb)
print(rb == output)