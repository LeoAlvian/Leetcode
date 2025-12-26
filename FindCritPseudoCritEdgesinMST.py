"""
Docstring for FindCritPseudoCritEdgesinMST

1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Solved
Hard
Topics
premium lock icon
Companies
Hint

Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.



Example 2:
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
"""

from collections import defaultdict
import heapq


# Kruskal Algorithm need UnionFind algorithm with time complexity O(e2)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1, n2):
        pn1, pn2 = self.find(n1), self.find(n2)

        if pn1 == pn2:
            return False
        if self.rank[pn1] >= self.rank[pn2]:
            self.par[pn2] = pn1
            self.rank[pn1] += self.rank[pn2]
        else:
            self.par[pn1] = pn2
            self.rank[pn2] += self.rank[pn1]
        
        return True

def findCritPseudoCritEdgesMSTKruskal(n, edges):
    for i, e in enumerate(edges):
        e.append(i)  # [n1, n2, weight, original_idx]
    
    edges.sort( key = lambda x : x[2] )
    mst_weight = 0
    uf = UnionFind(n)

    for n1, n2, w, i in edges:
        if uf.union(n1, n2):
            mst_weight += w
    
    critical, pseoudo = [], []
    for n1, n2, w, i in edges:
        # Try without cur edge
        weight = 0
        uf = UnionFind(n)
        for v1, v2, w2, i2 in edges:
            if i != i2 and uf.union(v1, v2):
                weight += w2
        if max(uf.rank) != n or weight > mst_weight:
            critical.append(i)
            continue
        
        # Try with cur edge
        uf = UnionFind(n)
        uf.union(n1, n2)
        weight = w
        for v1, v2, w2, i2 in edges:
            if uf.union(v1, v2):
                weight += w2
        if weight == mst_weight:
            pseoudo.append(i)
    
    return [critical, pseoudo]


# Dijkstra's algirithm with time complexity O(e2)
def findCriticalAndPseudoCriticalEdges(n, edges):
    for i, edge in enumerate(edges):
        edge.append(i)

    adj = defaultdict(list)
    for u, v, w, idx in edges:
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))

    def minimax(src, dst, exclude_idx):
        dist = [float('inf')] * n
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            max_w, u = heapq.heappop(pq)
            if u == dst:
                return max_w

            for v, weight, edge_idx in adj[u]:
                if edge_idx == exclude_idx:
                    continue
                new_w = max(max_w, weight)
                if new_w < dist[v]:
                    dist[v] = new_w
                    heapq.heappush(pq, (new_w, v))

        return float('inf')

    critical, pseudo = [], []
    for i, (u, v, w, idx) in enumerate(edges):
        if w < minimax(u, v, idx):
            critical.append(idx)
        elif w == minimax(u, v, -1):
            pseudo.append(idx)

    return [critical, pseudo]


n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
edges2 = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
edges3 = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
output = [[0,1],[2,3,4,5]]

fcp = findCritPseudoCritEdgesMSTKruskal(n, edges)
dj = findCriticalAndPseudoCriticalEdges(n, edges2)
print('Kruskal',fcp)
print('Dijkstra', dj)
print(output)