"""
11. Container With Most Water

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
"""

#              #              #
#              #              #     # 
#              #  #           #     # 
#              #  #     #     #     #
#              #  #     #  #  #     #
#              #  #     #  #  #  #  # 
#              #  #  #  #  #  #  #  #
#           #  #  #  #  #  #  #  #  #
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#           l                       r
# area (r - l) * min(height[l], height[r])

def containerWithMostWater(h):
    l, r = 0, len(h) - 1
    res = 0

    while l < r:
        area = (r - l) * min(h[l], h[r])
        res = max(res, area)

        if h[l] < h[r]:
            l += 1
        elif h[l] > h[r]:
            r -= 1
        else:
            if h[l + 1] > h[r - 1]:
                l += 1
            else:
                r -= 1
    
    return res


height = [1,8,6,2,5,4,8,3,7]
output = 49

print(containerWithMostWater(height))
print(output)