"""
983. Minimum Cost For Tickets

Solved
Medium
Topics
premium lock icon
Companies

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.



Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""


# Dynamic Programming Bottom-Up with time: O(n) and space: O(n)

def mincostTickets(days, costs):
    N = len(days)
    dp = ([float('inf')] * N) + [0]

    for i in reversed(range(N)):
        j = i
        for cost, duration in zip(costs, [1, 7, 30]):
            while j < N and days[j] < days[i] + duration:
                j += 1
            dp[i] = min(dp[i], dp[j] + cost)
    
    return dp[0]
    

# We make a dp array to store the minimum cost for every possible ticket and duration
# [1,4,6,7,8,20]
# [0,0,0,0,0, 0,0]
# Then we iterate in reverse order and add possible cost and duration and take the minimum and store it in the dp array
# [1, 4, 6, 7, 8, 20]       1 day, 2 cost
# [0, 0, 0, 0, 0, 2, 0]     0 + 2 = 2
#                ij
# [1, 4, 6, 7, 8, 20]       7 day, 7 cost
# [0, 0, 0, 0, 0, 2, 0]     0 + 7 = 7  min 2, 7
#                ij
# [1, 4, 6, 7, 8, 20]       30 day, 15 cost
# [0, 0, 0, 0, 0, 2, 0]     0 + 15 = 15 min 2, 15
#                ij
#
#
# [1, 4, 6, 7, 8, 20]       1 day, 2 cost
# [0, 0, 0, 0, 4, 2, 0]     2 + 2 = 4
#              ij
# [1, 4, 6, 7, 8, 20]       7 day, 7 cost
# [0, 0, 0, 0, 4, 2, 0]     4 + 7 = 2
#              ij
# [1, 4, 6, 7, 8, 20]       30 day, 15 cost
# [0, 0, 0, 0, 4, 2, 0]     2 + 15 = 17 min 4, 17
#              i  j



days = [1,4,6,7,8,20]
costs = [2,7,15]
output = 11

res = mincostTickets(days, costs)

print(res)
print(output)