"""
1235. Maximum Profit in Job Scheduling

Solved
Hard
Topics
premium lock icon
Companies
Hint

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:

            [  40   ]          profit
        [  10   ]
    [   50  ][    70    ]
    1   2   3   4   5   6

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.




Example 2:

        [     20    ]
            [            100            ]
    [   20  ]   [   70  ][    60    ]
    1   2   3   4   5   6   7   8   9   10

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.



Example 3:

    [     4     ]
    [   6   ]
    [ 5 ]
    1   2   3   4

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
"""


# Dynamic Programming (Top-Down) + Binary Search
# Intuition
# The linear scan to find the next non-overlapping job can be optimized using binary search. Since jobs are sorted by start time, we can binary search for the first job whose start time is at least the current job's end time.

# Algorithm
# 1. Sort intervals by start time.
# 2. Use recursion with memoization.
# 3. At each index, either skip the job or take it.
# 4. When taking a job, use binary search to find the next non-overlapping job.
# 5. Return the maximum profit.


import bisect

def jobScheduling(startTime, endTime, profit):
    intervals = sorted(zip(startTime, endTime, profit))
    # intervals = [(1, 3, 20), (2, 5, 20), (3, 10, 100), (4, 6, 70), (6, 9, 60)]
    cache = {}

    def dfs(i):
        if i == len(intervals):
            return 0
        if i in cache:
            return cache[i]
        
        # Don't include the job
        res = dfs(i + 1)

        # Include the job
        j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
        res = max(res, intervals[i][2] + dfs(j))
        cache[i] = res
        # {4: 60}
        # {4: 60, 3: 130}
        # {4: 60, 3: 130, 2: 130}
        # {4: 60, 3: 130, 2: 130, 1: 130}
        # {4: 60, 3: 130, 2: 130, 1: 130, 0: 150}
        return res

    return dfs(0)

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
output = 150

res = jobScheduling(startTime, endTime, profit)

print(res)
print(output)