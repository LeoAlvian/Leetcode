"""
Islands and Treasure

Medium
Topics
Company Tags
Hints

This "Islands and Treasure" is a "Walls And Gates" problem on leetcode

You are given a m × n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

  [1,-1,0, 1]
  [1, 1,1,-1]
  [1,-1,1,-1]
  [0,-1,1, 1]


Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0, 1],
  [2, 2,1,-1],
  [1,-1,2,-1],
  [0,-1,3, 4]
]




Example 2:

  [0,-1]
  [1, 1]

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1, 2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""


# Use BFS to solve this problem from the tresures and work all the way back and calculate every tile or grid based on the distance from the treasures

from collections import deque

def islandsAndTreasure(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set()
    q = deque()

    def addRoom(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or rooms[r][c] == -1 or (r, c) in visit:
            return
        visit.add((r, c))
        q.append([r, c])

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append([r, c])
                visit.add((r, c))

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = dist
            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c + 1)
            addRoom(r, c - 1)
        dist += 1



#   [1,-1,0, 1]
#   [1, 1,1,-1]
#   [1,-1,1,-1]
#   [0,-1,1, 1]


rooms = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

output = [
  [3,-1,0, 1],
  [2, 2,1,-1],
  [1,-1,2,-1],
  [0,-1,3, 4]
]

islandsAndTreasure(rooms)

print(rooms)
print(output)