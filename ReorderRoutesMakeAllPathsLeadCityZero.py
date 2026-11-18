"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

Solved
Medium
Topics
premium lock icon
Companies
Hint

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:

    From:
       ---------> (1) --------> (3) <-------- (2)
      /
    (0) <------ (4) --------> (5)

    To:
       --------- (1) <-------- (3) <-------- (2)
      /
     v
    (0) <------ (4) <-------- (5)

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).




Example 2:

    From:
    (0) <------ (1) --------> (2) <------ (3) --------> (4)

    To:
    (0) <------ (1) <-------- (2) <------ (3) <-------- (4)

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).




Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:

2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""




def minReorder(n, connections):
    # connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    edges = { (a, b) for a, b in connections }
    # edges {(0, 1), (4, 0), (2, 3), (4, 5), (1, 3)}
    neighbors = { city:[] for city in range(n)}
    # neighbors {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    visit = set()
    change = 0

    for a, b in connections:
        neighbors[a].append(b)
        neighbors[b].append(a)
    # neighbors 2 {0: [1, 4], 1: [0, 3], 2: [3], 3: [1, 2], 4: [0, 5], 5: [4]}

    def dfs(city):
        nonlocal change
        visit.add(city)
        for neighbor in neighbors[city]:
            if neighbor in visit:
                continue
            if (neighbor, city) not in edges:
                change += 1
            dfs(neighbor)

    dfs(0)
    return change



def minReorderII(n, connections):
    # connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    seen = [False] * n
    # seen = [False, False, False, False, False, False]
    ans = 0
    seen[0] = True
    #           T      T     T      T      T      T
    # seen = [True, False, False, False, False, False]
    # q = connections
    while connections:
        newq = []
        for src, dst in connections:
            if seen[src]:
                seen[dst] = True
                ans += 1
            elif seen[dst]:
                seen[src] = True
            else:
                newq.append((src, dst))
        # Reverse the order of unprocessed connections for the next iteration
        connections = newq[::-1]
        print('connections', connections)
    return ans



    #    ---------> (1) --------> (3) <-------- (2)
    #   /
    # (0) <------ (4) --------> (5)

    #    --------- (1) <-------- (3) <-------- (2)
    #   /
    #  v
    # (0) <------ (4) <-------- (5)

    # edges {(0, 1), (4, 0), (2, 3), (4, 5), (1, 3)}
    # neighbors 2 {0: [1, 4], 1: [0, 3], 2: [3], 3: [1, 2], 4: [0, 5], 5: [4]}

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
output = 3

res = minReorder(n, connections)
res2 = minReorderII(n, connections)

print(res)
print(res2)
print(output)