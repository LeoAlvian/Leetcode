"""
802. Find Eventual Safe States

Solved
Medium
Topics
premium lock icon
Companies

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

Example 1:
Illustration of graph
     |-----------------------|
     |       |---------------|       |-------|
     |       |       |       |       |       |
     v       |       v       v       |       v
    [0]     [1]     [2]     [3]     [4]     [5]     [6]
     |       ^      ^ |                      ^
     |       |      | |                      |
     |--------------| |----------------------|

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.




Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
"""




# Solving it using DFS with time: O(v + e) and space: O(v + e)

def eventualSafeNodes(graph):
    n = len(graph)
    safe_node = {}
    res = []

    def dfs(node):
        if node in safe_node:
            return safe_node[node]
        safe_node[node] = False
        for nei in graph[node]:
            if not dfs(nei):
                return safe_node[node]
        safe_node[node] = True
        return safe_node[node]

    for i in range(n):
        if dfs(i):
            res.append(i)
    return res



# Using Topological Ordering with time: O(v + e) and space: O(v + e)
from collections import deque

def eventualSafeNodesII(graph):
    n = len(graph)
    outdegree = [0] * n
    parents = [[] for _ in range(n)]
    queue = deque()

    for node in range(n):
        outdegree[node] = len(graph[node])
        if outdegree[node] == 0:
            queue.append(node)
        for nei in graph[node]:
            parents[nei].append(node)

    while queue:
        node = queue.popleft()
        for parent in parents[node]:
            outdegree[parent] -= 1
            if outdegree[parent] == 0:
                queue.append(parent)

    res = []
    for node in range(n):
        if outdegree[node] <= 0:
            res.append(node)
    return res




graph = [[1,2],[2,3],[5],[0],[5],[],[]]
output = [2,4,5,6]

res = eventualSafeNodes(graph)
res2 = eventualSafeNodesII(graph)

print(res)
print(res2)
print(output)