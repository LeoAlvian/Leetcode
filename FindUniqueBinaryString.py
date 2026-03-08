"""
1980. Find Unique Binary String

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.



Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.



Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""



def findDifferentBinaryString(nums):
    strSet = {s for s in nums}

    def backtrack(i, cur):
        if i == len(nums):
            res = ''.join(cur)
            return None if res in strSet else res

        res = backtrack(i + 1, cur)
        if res: return res

        cur[i] = '1'
        res = backtrack(i + 1, cur)
        if res: return res


    return backtrack(0, ['0' for s in nums])



# Cantor's Diagonal Argument
# Cantor's diagonal argument provides an elegant O(n) solution
# Create an empty result string.
# For each index i from 0 to n-1:
# Look at character nums[i][i] (the diagonal).
# Append the opposite character: if it is '0', append '1'; if '1', append '0'.
# Return the result string.

def findDifferentBinaryStringII(nums):
    res = []

    for i in range(len(nums)):
        if nums[i][i] == '0':
            res.append('1')
        else:
            res.append('0')
    
    return ''.join(res)


nums = ["111","000","001"]
output = "101"


# The differences is the backtrack algorithm not gonna raise index out of range when we 
# add new binary combination, ex: nums = ["111","000","001", "010"], it just gonna add 
# more length to the output
print(findDifferentBinaryString(nums))
# but the algorithm below will raise an index out of range error
print(findDifferentBinaryStringII(nums))
print(output)