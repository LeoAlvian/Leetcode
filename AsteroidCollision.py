"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.



Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.



Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.



Example 4:

Input: asteroids = [3,5,-6,2,-1,4]
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

# Using Stack data structure to solve this problem
# asteroids = [3,5,-6,2,-1,4]
# output = [-6,2,4]
# stack = []
# Loop through asteroids and while if there's items in stack and 
# asteroids[i] is negative and stack[-1] is positive, if abs(asteroids[i]) > stack[-1]
# then pop from stack, else if abs(asteroids[i] < stack[-1]) destroy the asteroids[i]
# else pop from stack and destroy asteroids[i]
# Ex
# asteroids = [3,5,-6,2,-1,4], a = 3 
# stack = [3]
# asteroids = [3,5,-6,2,-1,4] a = 5
# stack = [3,5]
# asteroids = [3,5,-6,2,-1,4] a = -6
# stack = [-6]
# asteroids = [3,5,-6,2,-1,4] a = 2
# stack = [-6,3]
# asteroids = [3,5,-6,2,-1,4] a = -1
# stack = [-6,2]
# asteroids = [3,5,-6,2,-1,4] a = 4
# stack = [-6,2,4]
# return stack

def AsteroidCollision(asteroids):
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if abs(a) > stack[-1]:
                stack.pop()
            elif abs(a) < stack[-1]:
                a = 0
            else:
                stack.pop()
                a = 0
        
        if a:
            stack.append(a)
    
    return stack


asteroids = [3,5,-6,2,-1,4]
output = [-6,2,4]
ac = AsteroidCollision(asteroids)
print(ac)
print(output)