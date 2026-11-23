"""
207. Course Schedule

Solved
Medium
Topics
premium lock icon
Companies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.



Example 2:


Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.



Example 3:

               |----------------------|
               |                      v
    [0] ----> [1] -----> [3] ------> [4]
     |
     |------> [2]

      Prerequsiste Map          Indegree            Adjesency List
    | crs   |   pre    |    | idx  |  val  |       | src  |   nei   |
    |  0    |  [1, 2]  |    |  0   |   0   |       |  0   | [1, 2]  |
    |  1    |  [3, 4]  |    |  1   |   1   |       |  1   | [3, 4]  |
    |  2    |  []      |    |  2   |   1   |       |  2   | []      |
    |  3    |  [4]     |    |  3   |   1   |       |  3   | [4]     |
    |  4    |  []      |    |  4   |   2   |       |  4   | []      |

Input: numCourses = 5, prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
Output: true


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""



# Solving it using Topological Ordering (Khan Algorithm)
from collections import deque

def canFinish(n, pre):
    indegree = [0] * n
    adj = [[] for i in range(n)]
    for src, dst in pre:
        indegree[dst] += 1
        adj[src].append(dst)

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    finish = 0
    while q:
        node = q.popleft()
        finish += 1
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return finish == n




numCourses = 5
prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
output = True

res = canFinish(numCourses, prerequisites)

print(res)
print(output)