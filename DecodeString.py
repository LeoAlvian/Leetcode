"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"


Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"


Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

# Using Stack data structure
#
# We gonna add every character that is not ']' to the stack, when we find ']'
# we pop every character until we find '[' and add it to substr
# then we pop every character that is int after '[' and add it to k
# then we multiply k with substr and add it back to the stack until the end of the list
#
# Ex
#
# s = "3[a2[c]]"
# stack = ['3', '[', 'a', '2', '[', 'c', ]   -> we find ']'
# we keep popping from the stack until we find '[' and then we popping until int and 
# multiply them 
# substr = c, k = 2  -> 2 * c = cc
# stack = ['3', '[', 'a', 'cc', ]   -> we find ']'
# we keep popping from the stack until we find '[' and then we popping until int and 
# multiply them 
# substr = acc, k = 3  -> 3 * acc = accaccacc
def decodeStr(s):
    stack = []

    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()

            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            
            stack.append(int(k) * substr)

    return ''.join(stack)


s = "3[a2[c]]"
output = "accaccacc"
ds = decodeStr(s)
print(ds)
print(output)
print(ds == output)