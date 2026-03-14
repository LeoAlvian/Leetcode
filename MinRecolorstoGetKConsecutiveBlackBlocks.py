"""
2379. Minimum Recolors to Get K Consecutive Black Blocks

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.



Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""


# Using sliding window technique
# blocks = "W B B W W B B W B W" , k = 7
#           lr
# if r is W then increment recolor by 1
# recolor = 1
#
# blocks = "W B B W W B B W B W" , k = 7
#           l r
# if r is W then increment recolor by 1
# recolor = 1
#
# blocks = "W B B W W B B W B W" , k = 7
#           l   r
# if r is W then increment recolor by 1
# recolor = 1
#
# blocks = "W B B W W B B W B W" , k = 7
#           l     r
# if r is W then increment recolor by 1
# recolor = 2
#
# blocks = "W B B W W B B W B W" , k = 7
#           l       r
# if r is W then increment recolor by 1
# recolor = 3
#
# blocks = "W B B W W B B W B W" , k = 7
#           l         r
# if r is W then increment recolor by 1
# recolor = 3
#
# blocks = "W B B W W B B W B W" , k = 7
#           l           r
# if r is W then increment recolor by 1
# recolor = 3
# now the window size is len 7 so we shift left and right at the same time but we gonna
# need to decrease the left if it's white and store the minimum to result
#
# blocks = "W B B W W B B W B W" , k = 7
#             l           r
# if r is W and l is W then increment recolor by 1 but also decrement by 1
# recolor = 3
# res = min(k, recolor) => min(7, 3) => 3
#
# blocks = "W B B W W B B W B W" , k = 7
#               l           r
# if r is W and l is W then increment recolor by 1 but also decrement by 1
# recolor = 3
# res = 3
#
# blocks = "W B B W W B B W B W" , k = 7
#                 l           r
# if r is W and l is W then increment recolor by 1 but also decrement by 1
# recolor = 4
# res = 3
# we return res



def minimumRecolors(blocks, k):
    l = 0
    recolor = 0
    res = k

    for r in range(len(blocks)):
        if blocks[r] == 'W':
            recolor += 1
        if r - l + 1 == k:
            res = min(res, recolor)
            if blocks[l] == 'W':
                recolor -= 1
            l += 1
    
    return res


blocks = "WBBWWBBWBW"
k = 7
output = 3

print(minimumRecolors(blocks, k))
print(output)