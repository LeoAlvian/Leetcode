"""
210. Course Schedule II

Solved
Medium
Topics
premium lock icon
Companies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].



Example 2:

    [3] --------> [1] ------> [0] 
     |                         ^
     |----------> [2] ---------|

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].



Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]



Example 4:

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
Output: [4,3,1,2,0] or [2,4,3,1,0], both is valid answer
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""




# Using DFS with time: O(e + v) and space: O(e + v)
def findOrder(n, pre):
    adj = { i:[] for i in range(n) }
    for crs, p in pre:
        adj[crs].append(p)

    courses = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for p in adj[crs]:
            if not dfs(p):
                return False
        cycle.remove(crs)
        visit.add(crs)
        courses.append(crs)
        return True

    for crs in range(n):
        if not dfs(crs):
            return []
    return courses



# Solving it using Topological Ordering (Khan Algorithm) with time: O(e + v) and space: O(e + v)
from collections import deque

def findOrderTopological(n, prerequisites):
    indegree = [0] * n
    adj = [ [] for i in range(n) ]
    courses = []

    for crs, pre in prerequisites:
        indegree[crs] += 1
        adj[pre].append(crs)

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
            courses.append(i)

    visit = 0
    while q:
        crs = q.popleft()
        visit += 1
        for pre in adj[crs]:
            indegree[pre] -= 1
            if indegree[pre] == 0:
                q.append(pre)
                courses.append(pre)

    return courses if visit == n else []



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
output = [0,2,1,3]

# numCourses = 5
# prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
# output = [4,3,1,2,0] or [2,4,3,1,0]

res = findOrder(numCourses, prerequisites)
res2 = findOrderTopological(numCourses, prerequisites)

print(res)
print(res2)
print(output)