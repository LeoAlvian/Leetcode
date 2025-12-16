"""
Docstring for IPO

502. IPO

Solved
Hard
Topics
premium lock icon
Companies

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.



Example 2:
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""

# Using Heap / Priority Queue
#
# we gonna use max heap called maxProfit to sort the profit from the biggest to 
# smallest, and then have arr of capital, profit called minCapital to keep track of 
# capital that we can affort using our own capital w
# Loop k times and check all capital in minCapital if minCapital <= w, if it is then 
# we take the corespond profit and add it to w and keep going until we reach k times
#
# Ex: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# 
# k = 1
# minCapital = [[0,1], [1,2], [1,3]]  -> [capital, profits]
# maxProfit = []                      -> loop k times and check while minCapital[0][0] 
#                                     -><= w, push it to maxProfit
# minCapital[0][0] <= w = [0,1]       -> push it to maxProfit
# maxProfit = [1]                     -> took max profit to calculate w
# pop(1) -> 1 + w = 1 + 0 = 1
#
# k = 2
# minCapital = [[0,1], [1,2], [1,3]]  -> [capital, profits]
# maxProfit = []                      -> loop k times and check while minCapital[0][0] 
#                                     -><= w, push it to maxProfit
# minCapital[0][0] <= w = [1,2],[1,3] -> push it to maxProfit
# maxProfit = [3,2]                   -> took max profit to calculate w
# pop(3) -> 3 + w = 3 + 1 = 4


import heapq

def IPO(k, w, profits, capital):
    if w >= max(capital):
        return w + sum(heapq.nlargest(k, profits))
    
    maxProfit = []
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    minCapital.sort(key = lambda x : x[0])
    n = len(profits)
    cur = 0

    for i in range(k):
        while cur < n and minCapital[cur][0] <= w:
            p = minCapital[cur][1]
            heapq.heappush(maxProfit, -p)
            cur += 1

        if not maxProfit:
            break
        w += -1 * heapq.heappop(maxProfit)

    return w


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
output = 4
ip = IPO(k,w,profits,capital)
print(ip)
print(output)