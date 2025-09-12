"""
1851. Minimum Interval to Include Each Query

Description:
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].

Note: The length of an interval is calculated as right_i - left_i + 1.

Example 1:

Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]

Output: [2,2,3,5,1,-1]
Explanation:

Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
Query = 8: There is no interval containing 8.
"""

import heapq

Test1 = {'intervals' : [[1,3],[2,3],[3,7],[6,6]],  'queries' : [2,3,1,7,6,8], 'out': [2,2,3,5,1,-1]}


class Solution:
    def minInterval(self, intervals, queries):
        #sorting intervals
        intervals.sort()

        #create minHeap to store minimum size and hash map to store the result
        minHeap = []
        res, i = {}, 0

        #creating a copy of sorting queries without destroying the original
        #and loop through queries
        for q in sorted(queries):
            #loop through intervals that the queries are part of and add the
            #minimum size to the minHeap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            #loop through minHeap and removing the list that the queries
            #are not part of
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            #add minimum value from minHeap to the res if there is non add -1
            res[q] = minHeap[0][0] if minHeap else -1
        
        #return the mapping from res to the original queries
        return [res[q] for q in queries]
            


s = Solution()
res = s.minInterval(Test1['intervals'], Test1['queries'])
print('Test1', res == Test1['out'])