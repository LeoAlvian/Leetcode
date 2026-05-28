"""
1758. Minimum Changes To Make Alternating Binary String

Solved
Easy
Topics
premium lock icon
Companies
Hint

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.



Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.



Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
"""


def minOperations(s):
    count = 0 # start from 0

    for i in range(len(s)):
        if s[i] != ('1' if i % 2 else '0'):
            count += 1

        # Code above are the same as this code below just more conscise 
        # if i % 2:
        #     count += 1 if s[i] == '0' else 0
        # else:
        #     count += 1 if s[i] == '1' else 0

    return min(count, len(s) - count)



s = "1111"
output = 2

res = minOperations(s)

print(res)
print(output)