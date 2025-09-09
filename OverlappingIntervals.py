"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping."""

Test1 = {'inp': {'intervals' : [[1,2],[2,3],[3,4],[1,3]]}, 'out': 1}
Test2 = {'inp': {'intervals' : [[1,2],[1,2],[1,2]]}, 'out': 2}
Test3 = {'inp': {'intervals' : [[1,2],[2,3]]}, 'out': 0}



class Solution:
    def eraseOverlapIntervals(self, intervals):
        #sort the intervals
        intervals.sort(key = lambda i : i[0])
        #create result and last value of the first intervals variable
        result = 0
        lastEnd = intervals[0][1]
    
        #loop through the intervals
        for start, end in intervals[1:]:
            #check if the intervals[i][0] <= last value
            if start >= lastEnd:
                #yes : last value = intervals[i][1]
                lastEnd = end
            else:
                #no : update result and last value to be min or last value or intervalsl[i][1]
                result += 1
                lastEnd = min(lastEnd, end)
        #return result
        return result



s = Solution()
res = s.eraseOverlapIntervals(Test1['inp']['intervals'])
print('Test1', res == Test1['out'])
res = s.eraseOverlapIntervals(Test2['inp']['intervals'])
print('Test2', res == Test2['out'])
res = s.eraseOverlapIntervals(Test3['inp']['intervals'])
print('Test3', res == Test3['out'])