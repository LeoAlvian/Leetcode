"""
837. New 21 Game

Solved
Medium
Topics
premium lock icon
Companies

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.



Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.



Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:

0 <= k <= n <= 104
1 <= maxPts <= 104
"""



def new21Game(n, k, maxPts):
    if k == 0:
        return 1
    
    windowSum = 0
    for i in range(k, k + maxPts):
        windowSum += 1 if i <= n else 0
    
    dp = {}
    for i in range(k - 1, -1, -1):
        dp[i] = windowSum / maxPts
        remove = 0
        if i + maxPts <= n:
            remove = dp.get(i + maxPts, 1)
        windowSum += dp[i] - remove
    
    return dp[0]



# [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
#     k              n          max
# Calculate sum of the window from k - n and then calculate the spot before k with
# the sum of all possibilities devided by the maxPts, then store the result in spot
# before k and slide the window until we reach 0
#
# [0.6, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
#       k              n          max
#   k                          max
# since we reach 0 we return 

n = 6
k = 1
maxPts = 10
output = 0.60000


res = new21Game(n, k, maxPts)

print(res)
print(output)