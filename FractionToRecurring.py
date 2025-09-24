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

    # creat list name res and check if numerator or denominator is less than 0
    # if it is then append - to the res
    res = []
    if numerator < 0 or denominator < 0:
        res.append('-')

    # making numerator and denominator to be positive
    num, den = abs(numerator), abs(denominator)

    # Append string of num / den but only get the whole value
    res.append(str(num // den))
    # Check if there is a reminder if not then we can just return it
    reminder = num % den
    if reminder == 0:
        return ''.join(res)
    
    # If there's a reminder then we need to calculate it and append it to res
    # We also need to check if the reminder is reacurring
    # If there is, we need to put that in a parenthesis and return that
    res.append('.')
    # To check if the reminder is reacurring we use hashMap
    rem_map = {}

    # Loop while we have reminder and check if reminder already in hashMap
    # If so we need to add parenthesis in corresponding index
    # That's why we need to add len(res) so we can insert parenthesis in the
    # right position
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
        print('rm', rem_map)
        print('res', res)
        print('reminder', reminder)
    
    return ''.join(res)


numerator = 4 
denominator = 333
output = "0.(012)"

ftd = fractionToDecimal(numerator, denominator)
print(ftd)
print(ftd == output)