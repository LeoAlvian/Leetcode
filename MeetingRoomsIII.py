"""
2402. Meeting Rooms III

Solved
Hard
Topics
premium lock icon
Companies
Hint

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 



Example 2:
Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
 

Constraints:

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
All the values of starti are unique.
"""

import heapq

def meetingRoomIII(n, meetings):
    meetings.sort()

    available = [i for i in range(n)] # [0, 1, 2] meeting room number available
    used = [] # used room in pair (end_meeting, room_meeting)
    count = [0] * n # count how many times the meeting room used

    for start, end in meetings:
        # pop all used heap where used[0][0] <= start and push the room to available
        while used and start >= used[0][0]:
            _, room = heapq.heappop(used)
            heapq.heappush(available, room)
        
        # if there is no available room we gonna pooping from used and then calculate the waiting time for the new meeting to be inputted to the used heap again and push the room number to available
        if not available:
            end_meeting, room = heapq.heappop(used)
            end = end_meeting + (end - start)
            heapq.heappush(available, room)
        
        # Pop room from available heap and adding (end, room) to used heap and increment count[room] += 1
        room = heapq.heappop(available)
        heapq.heappush(used, (end, room))
        count[room] += 1

    # return the the index of max count
    return count.index(max(count))


n = 3
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
output = 1
mr3 = meetingRoomIII(n, meetings)

print(mr3)
print(output)