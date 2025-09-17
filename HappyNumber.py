"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Example 2:

Input: n = 101
Output: false
Explanation:
1^2 + 0^2 + 1^2 = 2
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4 (This number has already been seen)
"""

n = 19
output = True

n2 = 101
output2 = False


def happyNum(n):
    # uset set to store visited number and to see if the number already calculated
    visited = set()

    # loop until number are 1 or number in visited
    while n not in visited:
        # add number to visited
        visited.add(n)
        print('visited', visited)
        # calculate the sum of the squares number
        n = sumOfSquares(n)
        print('n',n)

        # check if it's one, return true otherwise return false
        if n == 1:
            return True
    return False

def sumOfSquares(n):
    out = 0

    # loop until n == 0
    while n:
        # n mod 10 to get the decimal value and then n // 10 to get the remining
        # add the result to output
        mod = n % 10
        out += mod ** 2
        n = n // 10
    return out


print(happyNum(n2))