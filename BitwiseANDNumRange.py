"""
Docstring for BitwiseANDNumRange

201. Bitwise AND of Numbers Range

Solved
Medium
Topics
premium lock icon
Companies

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


Example 1:
Input: left = 5, right = 7
Output: 4


Example 2:
Input: left = 10, right = 15
Output: 8


Example 3:
Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
"""


# The idea is loop until the right is equal to left and bit shift it by one if not equal
# then keep track of how many shift we did in this case we gonna use i
# Ex:
#
# i = 0
# 10 => 1010
# 15 => 1111
# Loop while they are not equal and bit shift to left
#
# i = 1
# 10 => 1010 >> 1 = 101 => 5
# 15 => 1111 >> 1 = 111 => 7
#
# i = 2
# 5 => 101 >> 1 = 10 => 2
# 7 => 111 >> 1 = 11 => 3
#
# i = 3
# 2 => 10 >> 1 = 1 => 1
# 3 => 11 >> 1 = 1 => 1
# Because they are equal we exit the loop then return the number with a bit shift to
# the right by ith time
#
# return 1 << i => 1 << 3 => 1000 = 8

def bitwiseAndNumRange(left, right):
    i = 0

    while left != right:
        left >>= 1
        right >>= 1
        i += 1
    
    return left << i


left = 10
right = 15
output = 8

bnr = bitwiseAndNumRange(left, right)

print(bnr)
print(output)