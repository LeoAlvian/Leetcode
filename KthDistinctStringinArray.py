"""
Docstring for KthDistinctStringinArray

2053. Kth Distinct String in an Array

Solved
Easy
Topics
premium lock icon
Companies
Hint

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 



Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.



Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
"""


# This function Uses two Hash Set, distinct and seen, distinct is to keep track of 
# distinct element in an arr and seen is to keep track if there is more a third same 
# element appear in an arr, because if we didn't use seen if there is 3 of the same 
# element, the third one gonna be inserted to the distinct as a new set and we didn't 
# want that

def kthDistinctStr(arr, k):
    distinct, seen = set(), set()

    for s in arr:
        if s in distinct:
            distinct.remove(s)
            seen.add(s)
        elif s not in seen:
            distinct.add(s)
    
    for s in arr:
        if s in distinct:
            k -= 1
            if k == 0:
                return s
    
    return ''



arr = ["d","b","c","b","c","a"]
k = 2
output = "a"

kd = kthDistinctStr(arr, k)

print(kd)
print(output)