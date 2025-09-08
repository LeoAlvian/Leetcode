"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.
"""

Test1 = {'inp': {'intervals' : [[1,3],[4,6]], 'newInterval' : [2,5]}, 'out': [[1,6]]}
Test2 = {'inp': {'intervals' : [[1,2],[3,5],[6,7],[8,10],[12,16]], 'newInterval' : [4,8]}, 'out': [[1,2],[3,10],[12,16]]}

class Solution:
    def insert(self, intervals = [1,3], newInterval = [1,2]):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res

s = Solution()
result = s.insert(Test1['inp']['intervals'], Test1['inp']['newInterval'])
print('Test1', result == Test1['out'])
result = s.insert(Test2['inp']['intervals'], Test2['inp']['newInterval'])
print('Test2', result == Test2['out'])