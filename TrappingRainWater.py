"""
42. Trapping Rain Water

Solved
Hard
Topics
premium lock icon
Companies

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9


Example 3:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


def trappingRainWater(h):
    if not h: return 0
    
    l, r = 0, len(h) - 1
    leftMax, rightMax = h[l], h[r]
    res = 0

    while l < r:
        if leftMax <= rightMax:
            l += 1
            leftMax = max(leftMax, h[l])
            res += leftMax - h[l]
        else:
            r -= 1
            rightMax = max(rightMax, h[r])
            res += rightMax - h[r]
    
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6

trw = trappingRainWater(height)

print(trw)
print(output)