"""
752. Open the Lock

Solved
Medium
Topics
premium lock icon
Companies
Hint

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".


Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".


Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

# Using graph and breadth-first search algorithm

from collections import deque

def openLock(deadends, target):
    if '0000' in deadends:
        return -1
    
    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) + 9) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
        
        return res

    q = deque()
    q.append(['0000', 0])
    visited = set(deadends)

    while q:
        lock, turn = q.popleft()
        if lock == target:
            return turn
        for child in children(lock):
            if child not in visited:
                visited.add(child)
                q.append([child, turn + 1])
    
    return -1





def openLockII(deadends, target):
    vis = set(deadends)
    source = '0000'
    if source in vis:
        return -1
    if source == target:
        return 0

    vis.add(source)
    vis.add(target)
    nxt_c = {
        '0': '19',
        '1': '20',
        '2': '31',
        '3': '42',
        '4': '53',
        '5': '64',
        '6': '75',
        '7': '86',
        '8': '97',
        '9': '08',
    }
    front = {'0000'}
    back = {target}
    move = 0
    while front and back:
        if len(front) > len(back):
            front, back = back, front
        move += 1
        nxt_front = set()
        for cur in front:
            cur_list = list(cur)
            for i, ch in enumerate(cur_list):
                for c in nxt_c[ch]:
                    cur_list[i] = c
                    nxt = ''.join(cur_list)
                    if nxt in back:
                        return move
                    if nxt not in vis:
                        vis.add(nxt)
                        nxt_front.add(nxt)
                    cur_list[i] = ch
        front = nxt_front
    
    return -1





deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
output = 6

ol = openLock(deadends, target)
ol2 = openLockII(deadends, target)

print(ol)
print(ol2)
print(output)