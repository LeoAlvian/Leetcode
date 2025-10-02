"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
Input: strs = ["bat","bag","bank","band"]
Output: "ba"


Example 3:
Input: strs = ["dance","dag","danger","damage"]
Output: "da"


Example 4:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def longestPrefix(strs):
    res = ''

    for i in range(len(strs[0])):
        for s in strs[1:]:
            print('s',s)
            print('i',i)
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    
    return res

strs = ["dance","dag","danger","damage"]
output ="da"
lp = longestPrefix(strs)
print(lp)