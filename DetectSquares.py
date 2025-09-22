"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

Example 1:

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
"""

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        # to store all point in list
        self.points = []
        # store how many point with the same coordinate ex: [0][2] with x = 0 and y = 2
        self.pointsCount = defaultdict(lambda: defaultdict(int))
    
    def add(self, point):
        # add all point to points and counts duplicates coordinate
        self.points.append(point)
        self.pointsCount[point[0]][point[1]] += 1

    def count(self, point):
        res = 0
        px, py = point
        # loop through all points and see if we can form a square
        for x, y in self.points:
            # checking if we can form a square, if x - px is != with y - py
            # or x == px or y == py then the point is not square then we just skip the loop
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            # else we count by multiplying all points that is diagonal to the input
            res += self.pointsCount[x][py] * self.pointsCount[px][y]
        return res


ds = DetectSquares()
inp = [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]
ds.add([3, 10])
ds.add([11, 2])
ds.add([3, 2])
r1 = ds.count([11, 10])
r2 = ds.count([14, 8])
ds.add([11, 2])
r3 = ds.count([11, 10])
out = [r1, r2, r3]
print('output',out)
output = [1, 0, 2]
print(out == output)