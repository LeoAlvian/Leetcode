"""
You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:

Input: num1 = "3", num2 = "4"
Output: "12"


Example 2:

Input: num1 = "111", num2 = "222"
Output: "24642"


Example 3:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""


num1 = "123"
num2 = "456"
output = "56088"


# this is not allowed because we convert input directly also if num1 or num2 is a really big number this cannot work because of int 32 bits ro 64 bits
# def multiplyStr(num1, num2):
#     return str(int(num1) * int(num2))

def multiplyStr(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    
    num1, num2 = num1[::-1], num2[::-1]
    res = [0] * (len(num1) + len(num2))

    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            pos = i1 + i2
            res[pos] += digit
            res[pos + 1] += res[pos] // 10
            res[pos] = res[pos] % 10
    
    res, zero = res[::-1], 0
    while zero < len(res) and res[zero] == 0:
        zero += 1
    
    res = map(str, res[zero:])
    return ''.join(res)



result = multiplyStr(num1, num2)
print(result)