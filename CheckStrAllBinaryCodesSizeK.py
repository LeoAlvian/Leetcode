"""
1461. Check If a String Contains All Binary Codes of Size K

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.



Example 2:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 



Example 3:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

Constraints:

1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
"""

# Example
# Input: s = "00110110", k = 2
# Initialize empty set → seen = {}
# Slide window of size 2: (1 << k) with k = 2
# Window	Add to set	   Set after step
# "00"	       add	        {"00"}
# "01"	       add	        {"00","01"}
# "11"	       add	        {"00","01","11"}
# "10"	       add	        {"00","01","11","10"} → size = 4 = 2^2 → return True

# Input: s = "0110", k = 2
# Windows: "01", "11", "10"
# Set: {"01","11","10"} → size = 3 < 4 → return False

def hasAllCodes(s, k):
    seen = set()
    target = 1 << k # target = 2^k

    for i in range(len(s) - k + 1):
        subs = s[i:i+k]
        seen.add(subs)
        if len(seen) == target:
            return True
    
    return len(seen) == target



s = "00110110"
k = 2
output = True

print(hasAllCodes(s, k))
print(output)