"""
Docstring for EvaluateDivision

399. Evaluate Division

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0



Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]



Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

# Use Graph (BFS) to solve this problem
#
# equations = [["a","b"],["b","c"],["bc","cd"], ["b", "bc"]]
# values    = [   1.5   ,   2.5   ,    5.0    ,     0.2] 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"], ["cd", "a"]]
#
# From equations, values we told that a/b = 1.5, b/c = 2.5, bc/cd = 5
# We gonna use graph and map all the equations to the graph and result as a weight
#
#      1.5      2.5
# [a]  ->  [b]  ->  [c]
#              \ 0.2      5.0
#                ->  [bc]  ->  [cd]
#
# We need to make the reverse weight of the graph by dividing 1 / weight
# a -> b = 1.5  /  a <- b = 1 / 1.5
#
#     0.67      0.4
# [a]  <-  [b]  <-  [c]
#              \ 5.0       0.2
#                <-  [bc]  <-  [cd]
#
# We can do that my mapping all adjecency node with each other
# adj = {
# 'a': [('b', 1.5)], 
# 'b': [('a', 0.67), ('c', 2.5), ('bc', 0.2)], 
# 'c': [('b', 0.4)], 'bc': [('cd', 5.0), ('b', 5.0)], 
# 'cd': [('bc', 0.2)]
# }
#
# Them loop through the query and use BFS to traverse through all the node and add 
# all the weight while we traverse through it


from collections import defaultdict, deque

def evalDivision(equat, val, quer):
    adj = defaultdict(list)  # Map a -> [b, a/b]
    for i, eq in enumerate(equat):
        a, b = eq
        adj[a].append([b, val[i]])
        adj[b].append([a, 1 / val[i]])

    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1

        q, visit = deque(), set()
        q.append([src, 1])
        visit.add(src)

        while q:
            n, w = q.popleft()
            if n == target:
                return w
            for nei, weight in adj[n]:
                if nei not in visit:
                    q.append([nei, round(w * weight, 2)])
                    visit.add(nei)
        
        return -1
    
    return [bfs(q1, q2) for q1, q2 in quer]



equations = [["a","b"],["b","c"],["bc","cd"], ["b", "bc"]]
values    = [   1.5   ,   2.5   ,    5.0    ,     0.2] 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"], ["cd", "a"]]
output = [3.75000,0.40000,5.00000,0.20000, 0.67]
ed = evalDivision(equations, values, queries)
print(ed)
print(output)