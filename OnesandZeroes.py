"""
474. Ones and Zeroes

Solved
Medium
Topics
premium lock icon
Companies

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.



Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""


# Solving Using 2D-Array manipulation with time: O(2^n) and space(n) for recursion stack.

# Algorithm
# 1. Preprocess each string to count its zeros and ones, storing in an array arr.
# 2. Define a recursive function dfs(i, m, n) that returns the maximum strings we can select starting from index i with m zeros and n ones remaining.
# 3. Base case: If i reaches the end of the array, return 0.
# 4. At each index, we have two choices:
#   - Skip the current string: dfs(i + 1, m, n).
#   - Include the current string (if affordable): 1 + dfs(i + 1, m - zeros, n - ones).
# 5. Return the maximum of both choices.

def findMaxForm(strs, m, n):
    zero_one = [[0, 0] for i in range(len(strs))]
    # Create an array of how many 0's and 1's in the specific index of strs
    # zero_one = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i, s in enumerate(strs):
        for c in s:
            zero_one[i][ord(c) - ord('0')] += 1
    # zero_one = [[1, 1], [3, 1], [2, 4], [0, 1], [1, 0]]
    
    def dfs(i, m, n):
        if i == len(strs):
            return 0
        
        # Not Include the current strs
        res = dfs(i + 1, m, n)
        # If m >= the sum of next 0's in the array and n >= the sum of next 1's in the array
        if m >= zero_one[i][0] and n >= zero_one[i][1]:
            # Include the current strs
            res = max(res, 1 + dfs(i + 1, m - zero_one[i][0], n - zero_one[i][1]))
        return res

    return dfs(0, m, n)


strs = ["10","0001","111001","1","0"]
m = 5
n = 3
output = 4

res = findMaxForm(strs, m, n)

print(res)
print(output)