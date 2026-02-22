"""
868. Binary Gap

Solved
Easy
Topics
premium lock icon
Companies

Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

Example 1:
Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.



Example 2:
Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.



Example 3:
Input: n = 5
Output: 2
Explanation: 5 in binary is "101".
 

Constraints:

1 <= n <= 109
"""


def binaryGap(n):
    A = [i for i in range(32) if (n >> i) & 1]
    # A = [1, 2, 4] index of binary 22 that is 1, we get it from the right to left 
    # 22        = 0b10110
    # index     =   43210
    # index 1's =   4 21
    if len(A) < 2:
        return 0
    return max(A[i + 1] - A[i] for i in range(len(A) - 1))


# binary of 22 = 0b10110
n = 22
output = 2 

print(binaryGap(n))
print(output)