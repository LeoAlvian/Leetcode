"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 
Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"


Example 2:

Input: numerator = 2, denominator = 1
Output: "2"


Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
"""



def fractionToDecimal(numerator, denominator):
    if numerator == '0':
        return '0'

    res = []
    if numerator < 0 or denominator < 0:
        res.append('-')
    
    num, den = abs(numerator), abs(denominator)

    res.append(str(num // den))
    reminder = num % den
    if reminder == 0:
        return ''.join(res)
    
    res.append('.')
    rem_map = {}

    while reminder:
        if reminder in rem_map:
            pos = rem_map[reminder]
            res.insert(pos, '(')
            res.append(')')
            break

        rem_map[reminder] = len(res)
        reminder *= 10
        res.append(str(reminder // den))
        reminder %= den
    
    return ''.join(res)


numerator = 4 
denominator = 333
output = "0.(012)"

ftd = fractionToDecimal(numerator, denominator)
print(ftd)
print(ftd == output)