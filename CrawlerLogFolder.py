"""
1598. Crawler Log Folder

Solved
Easy
Topics
premium lock icon
Companies
Hint

The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:

   step 1     step 2     step 3      step 4
    d1          d1         d1         d1
                |                      |
                -> d2                  -> d21 

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.




Example 2:

  step 1     step 2         step 3         step 4       step 5
    d1          d1           d1              d1           d1
                |           |                |            |
                -> d2       -> d2            -> d2        -> d2
                                |                            |
                                -> d3                        -> d31

Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3


Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0
 

Constraints:

1 <= logs.length <= 103
2 <= logs[i].length <= 10
logs[i] contains lowercase English letters, digits, '.', and '/'.
logs[i] follows the format described in the statement.
Folder names consist of lowercase English letters and digits.
"""


# Using Stack to solve this problem with time: O(n) and space: O(n)

def minOperations(logs):
    stack = []

    for log in logs:
        if log == './':
            continue
        elif log == '../':
            if stack:
                stack.pop()
        else:
            stack.append(log)

    return len(stack)



logs = ["d1/","d2/","./","d3/","../","d31/"]
output = 3

res = minOperations(logs)

print(res)
print(output)