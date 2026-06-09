"""
1762. Buildings With an Ocean View - Explanation


Description
You are given an array of integers heights of size n representing a row of buildings, where heights[i] is the height of the ith building.

There is an ocean located to the far right of the buildings. A building has an ocean view if every building to its right is strictly shorter than it.

Return a list of indices (0-indexed) of the buildings that have an ocean view, sorted in increasing order.

Example 1:

Input: heights = [4,2,3,2,1]
Output: [0,2,3,4]



Example 2:

Input: heights = [1,3,2,4,2,5,1]
Output: [5,6]



Example 3:

Input: heights = [9,8,7,7,6,5,4,3]
Output: [0,1,3,4,5,6,7]


Constraints:

1 <= heights.length <= 100,000.
1 <= heights[i] <= 1,000,000,000

"""


# We loop in reverse order and then compare to the maxH if the building is taller we add it
# to the res, then update the maxH, then reverse before we return it 

def findBuildings(h):
    res = []
    maxH = 0

    for i in range(len(h) - 1, -1, -1):
        if h[i] > maxH:
            res.append(i)
            maxH = max(maxH, h[i])
    
    return res[::-1]


# We can make it slightly clever and we didn't need the maxH because the building that we
# append to res is always gonna the max height for that specific index
# Ex:
# heights = [4, 2, 3, 1]
# we loop in reverse, so heights[3] = 1 is the tallest so far
# then heights[2] = 3 is taller than heights[3] = 1 so 3 is tallest so far
# then heights[1] = 2 is shorter than heights[2] = 3 so 3 is still the tallest
# then heights[0] = 3 is taller than heights[2] = 3 so 4 is the tallest 

def findBuildingsII(h):
    res = [len(h) - 1]  # we populate res to be the last index of heights because it will always the tallest so far and has ocean view

    for i in range(len(h) - 2, -1, -1):
        if h[i] > h[res[-1]]:    # checking the cur heights with the last heigths index in res
            res.append(i)
    
    return res[::-1]



heights = [9,8,7,7,6,5,4,3]
output = [0,1,3,4,5,6,7]

res = findBuildings(heights)
res2 = findBuildingsII(heights)

print(res)
print(res2)
print(output)