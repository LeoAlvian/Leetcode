"""
Docstring for ExcelSheetColumnTitle

168. Excel Sheet Column Title

Solved
Easy
Topics
premium lock icon
Companies

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 


Example 1:
Input: columnNumber = 1
Output: "A"



Example 2:
Input: columnNumber = 28
Output: "AB"



Example 3:
Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
"""

# The way we solve this is by using math
# ex:
# 
# columnNumber = 28
# output = 'AB'
#
# we calculate the offset with columnNumber % 26 because 'A' is start from 1 so we need to 
# substract 1 first from the columnNumber before we do the calculation
# (28 - 1) % 26 => 1
# then we take ord('A') to get the ascii number of 'A' and then adding the offset
# then turn it back to character and then adding to the result
# res += chr(ord('A') + offset)
# then divide 28 by 26 for the next character
# columnNumber //= 26
# because we calculate from the right and then adding it to res so we need to reverse the 
# result before we return it


def excelSheetColumn(columnNumber):
    res = ''

    while columnNumber > 0:
        columnNumber -= 1
        offset = columnNumber % 26
        res += chr(ord('A') + offset) 
        columnNumber //= 26

    return res[::-1] 


columnNumber = 701
output = "ZY"

esc =excelSheetColumn(columnNumber)

print(esc)
print(output)