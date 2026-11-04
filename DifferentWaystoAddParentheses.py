"""
241. Different Ways to Add Parentheses

Solved
Medium
Topics
premium lock icon
Companies

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2



Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
"""



def diffWaysToCompute(expression):
    operations = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y
    }

    # "2*3-4*5"
    def backtrack(left, right):
        res = []

        for i in range(left, right + 1):
            op = expression[i]
            if op in operations:
                nums1 = backtrack(left, i - 1)
                nums2 = backtrack(i + 1, right)

                for n1 in nums1:
                    for n2 in nums2:
                        res.append(operations[op](n1, n2))

        if res == []:
            res.append(int(expression[left: right + 1]))
        return res

    return backtrack(0, len(expression) - 1)



expression = "2*3-4*5"
output = [-34,-14,-10,-10,10]

res = diffWaysToCompute(expression)

print(res)
print(output)