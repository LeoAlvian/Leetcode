"""
3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:

x[i] != x[j]
x[j] != x[k]
x[k] != x[i]
Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

 

Example 1:

Input: x = [1,2,1,3,2], y = [5,3,4,6,2]
Output: 14
Explanation:
Choose i = 0 (x[i] = 1, y[i] = 5), j = 1 (x[j] = 2, y[j] = 3), k = 3 (x[k] = 3, y[k] = 6).
All three values chosen from x are distinct. 5 + 3 + 6 = 14 is the maximum we can obtain. Hence, the output is 14.



Example 2:

Input: x = [1,2,1,2], y = [4,5,6,7]
Output: -1
Explanation:
There are only two distinct values in x. Hence, the output is -1.
 

Constraints:

n == x.length == y.length
3 <= n <= 105
1 <= x[i], y[i] <= 106
"""



def maxSumDistinctTriplet(x, y):
    best = [(None, float('-inf'))] * 3

    for xi, yi in zip(x, y):
        for i, (xb, yb) in enumerate(best):
            if xi == xb:
                if yi > yb:
                    best[i] = (xi, yi)
                    best.sort(key = lambda t : t[1], reverse = True)
                break
        else:
            if yi > best[0][1]:
                best = [(xi, yi), best[0], best[1]]
            elif yi > best[1][1]:
                best = [best[0], (xi, yi), best[1]]
            elif yi > best[2][1]:
                best[2] = (xi, yi)
    
    return sum(y for x, y in best) if best[2][1] > float('-inf') else -1


x = [1,2,1,3,2]
y = [5,3,4,6,2]
output = 14

res = maxSumDistinctTriplet(x, y)

print(res)
print(output)