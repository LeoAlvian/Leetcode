"""
973. K Closest Points to Origin - Explanation
Problem Link

Description
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are returned.)


Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).




Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.


Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
"""




# The Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))
# Where x1 is x coordinate, x2 is the origin in this case is 0
# and y is the y coordinate, y2 is the origin 0
# But since we only care about the closest distant the the origin (0,0) we didn't really care about the exact distance or the sqrt of the distance, we just need to find the smallest of (x1^2 + y1^2)

import heapq

def kClosest(points, k):
    minHeap = []
    res = []

    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
    heapq.heapify(minHeap)

    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1

    return res

points = [[0,2],[2,2]]
k = 1
output = [[0,2]]

res = kClosest(points, k)

print(res)
print(output)