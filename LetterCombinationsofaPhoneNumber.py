"""
17. Letter Combinations of a Phone Number

Solved
Medium
Topics
premium lock icon
Companies

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]



Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


# Solving it using Backtrack with time: O(n * 4^n) and space: O(n) extra space and O(4^n) 
# for the output list

def letterCombinations(digits):
    res = []
    keypad = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def dfs(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return

        for c in keypad[digits[i]]:
            dfs(i + 1, curStr + c)

    if digits:
        dfs(0, '')
    return res




def letterCombinationsII(digits):
    keypad = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    combinations = [""]
    for digit in digits:
        combinations = [prefix + letter for prefix in combinations for letter in keypad[digit]]
    return combinations if digits else []

digits = "23"
output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

res = letterCombinations(digits)
res2 = letterCombinationsII(digits)

print(res)
print(res2)
print(output)