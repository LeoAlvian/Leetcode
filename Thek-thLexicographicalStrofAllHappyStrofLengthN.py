"""
1415. The k-th Lexicographical String of All Happy Strings of Length n

Solved
Medium
Topics
premium lock icon
Companies
Hint

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".




Example 2:

Input: n = 3, k = 6
Output: "bac"
Explanation: The list ['aba', 'abc', 'aca', 'acb', 'bab', 'bac', 'bca', 'bcb', 'cab', 'cac', 'cba', 'cbc'] contains all happy strings of length 3. The sixth string is "bac".




Example 3:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.




Example 4:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100
"""


def getHappyString(n, k):
    total_happy = 3 * (2**(n - 1))
    # total_happy = 12

    if k > total_happy:
        return ""

    res = []
    choices = 'abc'
    left, right = 1, total_happy

    for i in range(n):
        cur = left
        partition = (right - left + 1) // len(choices)
        # partition = 12 // 3 = 4
        # partition: 1 - 4, 5 - 8, 9 - 12

        for c in choices:
            if k in range(cur, cur + partition):
                res.append(c)
                left = cur
                right = cur + partition - 1
                choices = 'abc'.replace(c, '')
                break
            cur += partition


    return ''.join(res)




# Using backtrack

def getHappyStringII(n, k):
    res = []

    def backtrack(path):
        if len(res) == k:
            return
        if len(path) == n:
            res.append(''.join(path))
            return

        for c in ('a','b','c'):
            if not path or path[-1] != c:
                path.append(c)
                backtrack(path)
                path.pop()

    backtrack([])
    if len(res) < k:
        return ''
    return res[-1]



n = 3
k = 6
output = "bac"
# happy_string = ['aba', 'abc', 'aca', 'acb', 'bab', 'bac', 'bca', 'bcb', 'cab', 'cac', 'cba', 'cbc']

res = getHappyString(n, k)
res2 = getHappyStringII(n, k)

print(res)
print(res2)
print(output)