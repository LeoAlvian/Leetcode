"""
881. Boats to Save People


Description
You are given an integer array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.



Example 1:

Input: people = [5,1,4,2], limit = 6
Output: 2

Explanation:
First boat [5,1].
Second boat [4,2].



Example 2:

Input: people = [1,3,2,3,2], limit = 3
Output: 4

Explanation:
First boat [3].
Second boat [3].
Third boat [1,2].
Fourth boat [2].

Constraints:

1 <= people.length <= 50,000
1 <= people[i] <= limit <= 30,000
"""


# Sort the people list and use greedy approach to solve this problem 
# ex 
# people = [1,3,2,3,2], limit 3
# people = [1,2,2,3,3] -> sorted
# Using two pointer left and right 
# 
# people = [1,2,2,3,3]   -> remain = limit - people[r] = 3 - 3 = 0
#           l       r       check if remind bigger or equal to people[l] if yes
#                           we increment left and add 1 to boat, boat = 1
# people = [1,2,2,3,3]   -> remain = 3 - 3 = 0
#           l     r         boat = 2
# people = [1,2,2,3,3]   -> remain = 3 - 2 = 1
#           l   r           because remining is equal to people[l], increment left
#                           boat = 3
# people = [1,2,2,3,3]   -> remain = 3 - 3 = 0
#             lr            boat = 4
# because l and r are in the same position return boat
def boatSave(people:list, limit:int):
    people.sort()
    boat = 0

    l, r = 0, len(people) - 1
    while l <= r:
        remain = limit - people[r]
        r -= 1
        boat += 1
        if l <= r and remain >= people[l]:
            l += 1
    
    return boat


people = [1,3,2,3,2]
limit = 3
output = 4
bs = boatSave(people, limit)
print(bs)
print(output)