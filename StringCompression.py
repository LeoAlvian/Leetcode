"""
443. String Compression
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""


# Using Two pointer technique with time complexity of O(n) and space O(1)
# 
# Ex
#
# k = 0, i = 0, n = len(chars)
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#           ki
# chars[k] = chars[i] 
# k += 1
# j = i + 1 = 0 + 1 = 1
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#           ij  k
# while j < n and chars[i] == chars[j]: j += 1
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#           i   jk
# str(j - i) => str(1 - 0) => str(1)
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#              ijk
#
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#              ijk
# chars[k] = chars[i] 
# k += 1
# j = i + 1 = 1 + 1 = 2
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#               i   jk
# while j < n and chars[i] == chars[j]: j += 1
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#               i   k                                           j
# str(j - i) => str(13 - 1) => str(12)
# chars = ["a","b","1","2","b","b","b","b","b","b","b","b","b"]
#                      k                                        ij

def compress(chars):
    n = len(chars)
    i = k = 0

    while i < n:
        chars[k] = chars[i]
        k += 1
        j = i + 1

        while j < n and chars[i] == chars[j]:
            j += 1
        
        if (j - i) > 1:
            print(j)
            for c in str(j - i):
                chars[k] = c
                k += 1
        
        i = j
    
    return k


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
output = 4
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

print(compress(chars))
print(chars)
res = ''.join(chars[:4])
print(res)
print(output)