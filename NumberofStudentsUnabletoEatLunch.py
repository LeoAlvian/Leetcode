"""
1700. Number of Students Unable to Eat Lunch

Solved
Easy
Topics
premium lock icon
Companies
Hint

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.



Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
 

Constraints:

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
"""



# Using Hash Map to count every 1's and 0's sandwiches
# {1 : 2, 0 : 2}

from collections import Counter

def countStudents(students, sandwiches):
    res = len(students)
    cnt = Counter(students)

    for s in sandwiches:
        if cnt[s]:
            res -= 1
            cnt[s] -= 1
        else:
            return res

    return res



# Implement what is saying in the description which removing students from the first queue
# and adding them to the end if they didn't like the sandwiches

from collections import deque

def countStudentsII(students, sandwiches):
    dq = deque(students)
    s = 0
    rotations = 0

    while dq and s < len(sandwiches):
        if dq[0] == sandwiches[s]:
            dq.popleft()
            s += 1
            rotations = 0
        else:
            dq.append(dq.popleft())
            rotations += 1

            if rotations == len(dq):
                break
    
    return len(dq)



students = [1,1,0,0]
sandwiches = [0,1,0,1]
output = 0 

res = countStudents(students, sandwiches)
res2 = countStudentsII(students, sandwiches)

print(res)
print(res2)
print(output)