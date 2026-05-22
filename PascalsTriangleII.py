"""
119. Pascal's Triangle II

Solved
Easy
Topics
premium lock icon
Companies

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

     [1]
    [1, 1]
  [1, 2, 1]
 [1, 3, 3, 1]

Input: rowIndex = 3
Output: [1,3,3,1]



Example 2:

    [1]

Input: rowIndex = 0
Output: [1]



Example 3:

    [1]
   [1, 1]

Input: rowIndex = 1
Output: [1,1]




Example 4:

     [1]
    [1, 1]
  [1, 2, 1]
 [1, 3, 3, 1]
[1, 4, 6, 4, 1]

Input: rowIndex = 4
Output: [1, 4, 6, 4, 1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""



def getRow(rowIdx):
    res = [1]

    for i in range(rowIdx):
        next_row = [0] * (len(res) + 1)
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j + 1] += res[j]

        res = next_row
    
    return res
    


rowIndex = 4 
output = [1, 4, 6, 4, 1]

res = getRow(rowIndex)

print(res)
print(output)