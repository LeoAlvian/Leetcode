"""
Graph Valid Tree

Medium
Topics
Company Tags
Hints

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.


Example 1:

            [0]
          /  |  \
        [1] [2] [3]
         |
        [4]

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true



Example 2:

            [0] 
          /  
        [1] --- [4]
        / \
       /   \
      /     \
    [2] --- [3]

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a_i, b_i < n
a_i != b_i
There are no self-loops or repeated edges.
"""




# Solving it using DFS with time: O(v + e) and space: O(v + e)

def validTree(n, edges):
    if not n:
        return True

    adj = { i:[] for i in range(n) }
    for src, dst in edges:
        adj[src].append(dst)
        adj[dst].append(src)

    visit = set()
    def dfs(node, prev):
        if node in visit:
            return False

        visit.add(node)
        for nei in adj[node]:
            if nei == prev:
                continue
            if not dfs(nei, node):
                return False
        return True

    return dfs(0, -1) and n == len(visit)



        #     [0]
        #   /  |  \
        # [1] [2] [3]
        #  |
        # [4]

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
output = True

res = validTree(n, edges)

print(res)
print(output)