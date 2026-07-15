"""
354. Russian Doll Envelopes

Solved
Hard
Topics
premium lock icon
Companies

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).



Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""

import bisect
# import bisect

# bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

# data = [1, 2, 4, 4, 4, 5, 7]
# index = 0  1  2  3  4  5  6

# idx = bisect.bisect_left(data, 4)
# print(idx)  # Output: 2

# idx = bisect.bisect_left(data, 3)
# print(idx)  # Output: 2

# bisect_left: Points before (to the left of) any existing matching values.
# bisect_right (or bisect): Points after (to the right of) any existing matching values.

def maxEnvelopes(envelopes):
    # envelopes = [[5, 4], [6, 4], [6, 7] ,[2, 3]]
    envelopes.sort(key = lambda x : (x[0], -x[1]))
    # envelopes = [[2, 3], [5, 4], [6, 7], [6, 4]]

    def lis(heights):
        # heights = [3, 4, 7, 4]
        dp = [heights[0]]
        # dp = [3]
        # LIS = Longest Increasing Subsequence
        LIS = 1

        for i in range(1, len(heights)):
            if dp[-1] < heights[i]:
                dp.append(heights[i])
                LIS += 1
                continue
            idx = bisect.bisect_left(dp, heights[i])
            dp[idx] = heights[i]
        
        return LIS

    return lis([e[1] for e in envelopes])


envelopes = [[5,4],[6,4],[6,7],[2,3]]
output = 3

res = maxEnvelopes(envelopes)

print(res)
print(output)