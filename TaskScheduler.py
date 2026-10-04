"""
621. Task Scheduler

Solved
Medium
Topics
premium lock icon
Companies
Hint

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.




Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.





Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""



# Using Max Heap and Queue with time: O(m) and space: O(1) since we have at most 26 different characters
# where m is the number of tasks 

from collections import deque, Counter
import heapq

def leastInterval(tasks, n):
    count = Counter(tasks)
    # tasks = ["A","C","A","B","D","B"]
    # Counter({'A': 2, 'B': 2, 'C': 1, 'D': 1})
    maxHeap = [-cnt for cnt in count.values()]
    # maxHeap = [-2, -1, -2, -1]
    heapq.heapify(maxHeap)

    time = 0
    q = deque() # pair of [-cnt, idleTime]
    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = heapq.heappop(maxHeap) + 1
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time


tasks = ["A","C","A","B","D","B"]
n = 1
output = 6

res = leastInterval(tasks, n)

print(res)
print(output)