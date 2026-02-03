"""
Docstring for GroupShiftedStrings

Group Shifted Strings

Medium
Company Tags

Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".

Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".

We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-

You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.




Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]



Example 2:
Input: strings = ["a"]
Output: [["a"]]



Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""


# 1. For each string, compute a hash key by calculating the difference between 
# consecutive characters. Use modulo 26 to handle wrap-around.
# 2. Use a hash map where the key is this computed hash and the value is a list of 
# strings that share this pattern.
# 3. Iterate through all input strings, compute their hash key, and add each string to 
# the corresponding group in the hash map.
# 4. Return all the grouped lists from the hash map.
from collections import defaultdict

def groupShiftedStr(strs):
    # 1. For each string, compute a hash key by calculating the difference between 
    # consecutive characters. Use modulo 26 to handle wrap-around.
    def hashKey(s):
        key = []
        for a, b in zip(s, s[1:]):
            key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
        return ''.join(key)

    # 2. Use a hash map where the key is this computed hash and the value is a list of 
    # strings that share this pattern.
    groupKey = defaultdict(list)
    for s in strs:
        keyMap = hashKey(s)

        # 3. Iterate through all input strings, compute their hash key, and add each 
        # string to the corresponding group in the hash map.
        groupKey[keyMap].append(s)
    
    # group defaultdict(<class 'list'>, {'bb': ['abc', 'bcd', 'xyz'], 'ccb': ['acef'], 'z': ['az', 'ba'], '': ['a', 'z']})
    # 4. Return all the grouped lists from the hash map.
    return list(groupKey.values())



strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
output = [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]


print(groupShiftedStr(strings))
print(output)