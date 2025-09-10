"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true

Note:
(0,8),(8,10) is not considered a conflict at 8

Also the intervals are originally convert as a class object but for simpliciy we gonna use list
"""


Test1 = {'inp': {'intervals' : [[0,30],[5,10],[15,20]]}, 'out': False}
Test2 = {'inp': {'intervals' : [[5,8],[9,15]]}, 'out': True}
Test3 = {'inp': {'intervals' : []}, 'out': True}


class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i : i[0])

        for i in range(1, len(intervals)):
            in0 = intervals[i - 1]
            in1 = intervals[i]

            if in1[0] < in0[1]:
                return False
        return True
    


s = Solution()
res = s.canAttendMeetings(Test1['inp']['intervals'])
print('Test1', res == Test1['out'])
res = s.canAttendMeetings(Test2['inp']['intervals'])
print('Test2', res == Test2['out'])
res = s.canAttendMeetings(Test3['inp']['intervals'])
print('Test3', res == Test3['out'])