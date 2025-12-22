"""
Docstring for MinimumHeightTrees

310. Minimum Height Trees

Solved
Medium
Topics
premium lock icon
Companies
Hint

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.



Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""


# We need to find the minimum height of a given tree and return its root
# We Use topological ordering and BFS
#
# Ex :
# n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#
#            [3]                     or                  [4]
#     /    /     \     \                              /       \ 
#   [0]  [1]     [2]   [4]                          [5]       [3]
#                         \                               /    |    \
#                         [5]                           [0]   [1]   [2]
#
# Both of graph above are valid because both have the same minimum height so the 
# output is gonna be
# output = [3, 4]

from collections import defaultdict, deque

def minHeightTrees(n, edges):
    if n == 1:
        return [0]
    
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    # adj = {1: [0, 2, 3], 0: [1], 2: [1], 3: [1]})
    # Map every neighbor of each node
    
    edge_cnt = {}
    leaves = deque()

    for src, neighbor in adj.items():
        edge_cnt[src] = len(neighbor)
        if len(neighbor) == 1:
            leaves.append(src)
    
    
    # edge_cnt = {1: 3, 0: 1, 2: 1, 3: 1}
    # count how many edge that connected to the src
    # leaves = deque([0, 2, 3])
    # add all node that has a edge_cnt of 1 to the leaves
    
    while leaves:
        if n <= 2:
            return list(leaves)
        for i in range(len(leaves)):
            node = leaves.popleft()
            n -= 1
            for nei in adj[node]:
                edge_cnt[nei] -= 1
                if edge_cnt[nei] == 1:
                    leaves.append(nei)
        

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
output = [3,4]
mh = minHeightTrees(n, edges)
print(mh)
print(output)