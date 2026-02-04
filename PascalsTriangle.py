"""
118. Pascal's Triangle

Solved
Easy
Topics
premium lock icon
Companies

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]



Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""


def pascalsTriangle(numRows):
    res = [[1]]
    if numRows == 1:
        return res
    res.append([1,1])
    if numRows == 2:
        return res
    
    for i in range(2, numRows):
        # take last arr from res to act as the top arr
        lastRes = res[-1]
        # create a temporary array of 1's with lenght of i + 1
        temp = [1] * (i + 1)
        # loop from 1 to 1 index before last because we not gonna calculate the begining
        # and the end of the arr
        for j in range(1, len(temp) - 1):
            # Adding the last element with current element on the top arr and store it 
            # in temp[j]
            temp[j] = lastRes[j - 1] + lastRes[j]
        res.append(temp)
    
    return res


numRows = 5
output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

pt = pascalsTriangle(numRows)

print(pt)
print(output)