"""
22. Generate Parentheses

Solved
Medium
Topics
premium lock icon
Companies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]



Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""


# Solving it using backtrack

def generateParenthesis(n):
    res = []
    stack = []

    def backtrack(openN, closeN):
        if openN == n and closeN == n:
            res.append(''.join(stack))
            return

        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(')')
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


n = 3
output = ["((()))","(()())","(())()","()(())","()()()"]

res = generateParenthesis(n)

print(res)
print(output)