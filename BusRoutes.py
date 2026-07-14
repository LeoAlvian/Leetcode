"""
815. Bus Routes

Solved
Hard
Topics
premium lock icon
Companies

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: - The best strategy is take the first bus to the bus stop 7
             - then take the second bus to the bus stop 6.




Example 2:

routes = [[7,12],[4,9,15],[6],[15,19],[9,12,13]], source = 7, target = 19
output = 4
Explanation: - The best strategy is take the first bus to the bus stop 12
             - then take the fifth bus to the bus stop 9
             - then take the second bus to the bus stop 15
             - then take the forth bus to the bus stop of 19.




Example 3:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""


# Algorithm:
# 1. If source equals target, return 0 (no bus needed).
# 2. Build a mapping from each stop to the list of bus routes that serve it.
# 3. Initialize BFS from the source stop, tracking visited stops and visited buses.
# 4. For each level of BFS (representing one bus ride):
#    - For each stop at the current level, check all buses that serve this stop.
#    - For each unvisited bus, add all its stops to the next BFS level.
#    - Mark buses and stops as visited to avoid revisiting.
# 5. If we reach the target stop, return the number of bus rides taken.
# 6. If BFS completes without finding the target, return -1.


from collections import defaultdict, deque


def numBusesToDestination(routes, source, target):
    if source == target:
        return 0
    
    buses = len(routes)
    stop_bus = defaultdict(list)
    for bus in range(buses):
        for stop in routes[bus]:
            stop_bus[stop].append(bus)
    # stop_bus = defaultdict(<class 'list'>, {7: [0], 12: [0, 4], 4: [1], 9: [1, 4], 15: [1, 3], 6: [2], 19: [3], 13: [4]})
    
    res = 0
    bus_seen = set()
    stop_seen = set([source])
    # stop_seen = {7}
    q = deque([source])
    # q = deque([7])
    while q:
        for i in range(len(q)):
            stop = q.popleft()
            if stop == target:
                return res
            for bus in stop_bus[stop]:
                if bus in bus_seen:
                    continue
                bus_seen.add(bus)
                for next_stop in routes[bus]:
                    if next_stop in stop_seen:
                        continue
                    stop_seen.add(next_stop)
                    q.append(next_stop)
        res += 1
    return -1



routes = [[7,12],[4,9,15],[6],[15,19],[9,12,13]]
source = 7
target = 19
output = 4

res = numBusesToDestination(routes, source, target)

print(res)
print(output)