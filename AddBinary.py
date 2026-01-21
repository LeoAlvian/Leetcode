"""
Docstring for AddBinary

67. Add Binary

Time complexity: 
O(max(m,n))
Space complexity: 
O(m+n)

Solved
Easy
Topics
premium lock icon
Companies

Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"


Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def addBinary(a, b):
    res = ''
    carry = 0

    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        # both of int(a[i]) and ord(b[i]) - ord('0') are doing the same thing
        digitA = int(a[i]) if i < len(a) else 0
        digitB = ord(b[i]) - ord('0') if i < len(b) else 0

        total = digitA + digitB + carry
        digit = str(total % 2)
        res = digit + res
        carry = total // 2
    
    if carry:
        res = '1' + res
    return res


a = "1010"
b = "1011"
output = "10101"

ab = addBinary(a, b)

print(ab)
print(output)