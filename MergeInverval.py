"""Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]
Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]"""

Test1 = {'inp': {'intervals' : [[1,3],[1,5],[6,7]]}, 'out': [[1,5],[6,7]]}
Test2 = {'inp': {'intervals' : [[1,2],[2,3]]}, 'out': [[1,3]]}



class Solution:
    def merge(self, intervals: [[1,2]]):
        #Sort the intervals
        intervals.sort(key = lambda i : i[0])
        #add first intervals to the new array
        output = [intervals[0]]

        #iterate through all intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            #check if the next intervals[0] <= with the end of value in new array
            if start <= lastEnd:
                #Yes, Merge them
                output[-1][1] = max(end, lastEnd)
            #No, Add to the new array
            else:
                output.append([start, end])
        #return new array
        return output



s = Solution()
result = s.merge(Test1['inp']['intervals'])
print('Test1', result == Test1['out'])
result = s.merge(Test2['inp']['intervals'])
print('Test2', result == Test2['out'])