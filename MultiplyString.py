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

def multiplyStr(num1, num2):
    return str(int(num1) * int(num2))



result = multiplyStr(num1, num2)
print(result)