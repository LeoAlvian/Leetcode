"""
1496. Path Crossing

Solved
Easy
Topics
premium lock icon
Companies
Hint

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.



Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""


def isPathCrossing(path):
    dirs = { 'N' : [0, 1], 'E' : [1, 0], 'S' : [0, -1], 'W' : [-1, 0],}
    visit = set()
    x, y = 0, 0

    for c in path:
        visit.add((x, y))
        dx, dy = dirs[c]
        x, y = x + dx, y + dy
        if (x, y) in visit:
            return True
    return False



path = "NESWW"
output = True

res = isPathCrossing(path)

print(res)
print(output)