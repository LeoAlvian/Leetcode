"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
"""

Test1 = {'inp': {'intervals' : [[0,40],[5,10],[15,20]]}, 'out': 2}
Test2 = {'inp': {'intervals' : [[4,9]]}, 'out': 1}
Test3 = {'inp': {'intervals' : [(1,5),(2,6),(3,7),(4,8),(5,9)]}, 'out': 4}



class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res


s = Solution()
res = s.minMeetingRooms(Test1['inp']['intervals'])
print('Test1', res == Test1['out'])
res2 = s.minMeetingRooms(Test2['inp']['intervals'])
print('Test2', res2 == Test2['out'])
res3 = s.minMeetingRooms(Test3['inp']['intervals'])
print('Test2', res3 == Test3['out'])