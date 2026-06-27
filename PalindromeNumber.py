"""
9. Palindrome Number

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.



Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.



Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.




Example 4:

Input: x = 101101
Output: true
Explanation: 101101 reads as 101101 from left to right and from right to left.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

def isPalindrome(x):
    if x < 0:
        return False

    div = 1
    while x >= div * 10:
        div *= 10
    
    while x:
        if x // div != x % 10:
            return False
        x = (x % div) // 10
        div /= 100
    
    return True


x = 101101
output = True

res = isPalindrome(x)

print(res)
print(output)