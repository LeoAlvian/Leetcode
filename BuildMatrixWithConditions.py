"""
Docstring for BuildMatrixWithConditions

2392. Build a Matrix With Conditions

Solved
Hard
Topics
premium lock icon
Companies
Hint

You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

 

Example 1:
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.



Example 2:
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
 

Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
"""

from collections import deque

# Solving it using topological ordering (Kahn's Algorithm) with time complexity O(k2 + n + m)
def builMatrix(k, rowCon, colCon):
    def kahn(edges):   # return list of topological order [2, 1, 3]
        indegree = [0] * (k + 1)
        adj = [[] for i in range(k + 1)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            indegree[n2] += 1
        
        order = []
        q = deque()
        for i in range(1, k + 1):
            if not indegree[i]:
                q.append(i)
        
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        
        return order


    row_order = kahn(rowCon)
    col_order = kahn(colCon)
    if len(row_order) != k or len(col_order) != k:
        return []

    map_row = {val: i for i, val in enumerate(row_order)}
    map_col = {val: i for i, val in enumerate(col_order)}
    res = [[0] * k for i in range(k)]
    for num in range(1, k + 1):
        r, c = map_row[num], map_col[num]
        res[r][c] = num
    
    return res



k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
output = [[0, 0, 1], [3, 0, 0], [0, 2, 0]] # or output = [[3,0,0],[0,0,1],[0,2,0]]
bm = builMatrix(k, rowConditions, colConditions)
print(bm)
print(output)