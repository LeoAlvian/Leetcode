"""
Docstring for Candy

135. Candy

Solved
Hard
Topics
premium lock icon
Companies

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.



Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.



Example 3:
cndy    = [2, 1, 3, 2, 1, 1, 2, 3]
ratings = [4, 3, 5, 4, 3, 3, 4, 5]
output = 15     
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""


def candy(r):
    n = len(r)
    res = [1] * n
    # res = [1, 1, 1, 1, 1, 1, 1, 1]

    # First pass loop we gonna check to the left side from the element, if they are bigger 
    # we change r[i] to be r[i - 1] + 1
    for i in range(1, n):
        if r[i] > r[i - 1]:
            res[i] = res[i - 1] + 1
    # res = [1, 1, 2, 1, 1, 1, 2, 3]
    
    # Second pass loop we check to the right side from the element, if they are bigger we change r[i] to be the max of itself and r[i + 1] + 1, why we set it to max because if the element at r[i] is already bigger than the left side from the first pass we want to keep that change
    # ex:    [3,4,2]
    # candy: [1,2,1]
    # 4 already bigger than 3 so 4 gonna have 2 candy from the first pass and on second 
    # pass we want to keep the max of itself and how many candy the 2 have because if in 
    # case there is more element after 2 and 2 is let say 2 then we want to get 2 + 1 
    # which is 3 for the 4's candy, like example below
    # ex:  res    = [3,4,2,1,0]
    # first pass  = [1,2,1,1,1]
    # second pass = [1,4,3,2,1]
    # return sum of it which is 11
    
    for i in range(n - 2, -1, -1):
        if r[i] > r[i + 1]:
            res[i] = max(res[i], res[i + 1] + 1)
    # res = [2, 1, 3, 2, 1, 1, 2, 3]

    return sum(res)


ratings = [4, 3, 5, 4, 3, 3, 4, 5]
output = 15 

print(candy(ratings))
print(output)