"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# this methods are slower, we gonna make faster one

# def plusOne(digits):
#     # reverse the list so we can do from the end of the list
#     digits = digits[::-1]
#     carry, i = 1, 0

#     # loop while we still have carry
#     while carry:
#         # check if i is not out of bound
#         if i < len(digits):
#             # check if digits is 9
#             if digits[i] == 9:
#                 digits[i] = 0
#             # if not then we just add them and exit the loop
#             else:
#                 digits[i] += 1
#                 carry = 0
        
#         # i out of bound and we still have carry so we add them to the front
#         # of the list
#         else:
#             digits.append(1)
#             carry = 0
#         i += 1

#     # reverse it back before we return them
#     return digits[::-1]


def plusOne(digits):
    # reverse the list so we can do from the end of the list
    digits = digits[::-1]
    carry = 1

    while carry:
        # loop until the end of the list
        for i in range(len(digits)):
            # check if current digit is 9
            if digits[i] == 9:
                digits[i] = 0
            # if not 9 we add one and reset carry also break of the loop immedietly
            else:
                digits[i] += 1
                carry = 0
                break
        # if we still have carry then we append them to the begining of the list
        if carry:
            digits.append(1)
            carry = 0
    
    # reverse the list back before we return them
    return digits[::-1]



digits = [9,9,9,9]
output = [1,0,0,0,0]
res = plusOne(digits)
print(res)