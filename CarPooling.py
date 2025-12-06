"""
Docstring for CarPooling

1094. Car Pooling

Solved
Medium
Topics
premium lock icon
Companies
Hint

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""

import heapq

# Using minHeap in python is gonna be O(nlogn) time complexity but if the input are 
# low in this case from 0 to 1000, then we can use a brute force method which gonna 
# give us O(n) time complexity

def carPooling(trips, cap):
    trips.sort( key = lambda t : t[1] )
    minHeap = [] # Store [end, numPas]
    curCap = 0

    for trip in trips:
        numPas, start, end = trip
        while minHeap and minHeap[0][0] <= start:
            curCap -= minHeap[0][1]
            heapq.heappop(minHeap)
        
        curCap += numPas
        if curCap > cap:
            return False
        heapq.heappush(minHeap, [end, numPas])
    
    return True

# Brute force method 
def carPoolingBruteForce(trips, cap):
    passChange = [0] * 1001

    for trip in trips:
        numPass, start, end = trip
        passChange[start] += numPass
        passChange[end] -= numPass
    
    curCap = 0
    for i in range(1001):
        curCap += passChange[i]
        if curCap > cap:
            return False
    
    return True


trips = trips = [[2,1,5],[3,3,7]]
capacity = 5
output = True
cp = carPooling(trips, capacity)
cpbf = carPoolingBruteForce(trips, capacity)
print('Min Heap :', cp)
print('Brute Force :', cpbf)
print('Expected Output :', output)