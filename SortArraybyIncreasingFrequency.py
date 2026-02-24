"""
1636. Sort Array by Increasing Frequency - Explanation


Description
You are given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.



Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.



Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Constraints:

1 <= nums.length <= 100.
-100 <= nums[i] <= 100.

"""


from collections import Counter

def frequencySort(nums):
    count = Counter(nums)
    # This function sort the arr by count[n] with increasing order but if there is 
    # two array with the same count we need to sort it in decreasing order but it was
    # increasing by default so we put negative number on n
    # Ex:
    # nums = [1,1,2,2,2,3,4]
    # count = Counter({2: 3, 1: 2, 3: 1, 4: 1})
    # nums.sort will sort with count[n] as a key because count[3] = 1 and count[4] = 1 
    # so we use the -n sort on key to sort it in decreasingly because sort function is 
    # naturally increasing sort, so 4: 1 first and then 3: 1 so 3 and 1: 2 and then 2: 3
    # result
    # nums = [4,3,1,1,2,2,2]
    
    nums.sort(key = lambda n : (count[n], -n))
    return nums



nums = [1,1,2,2,2,3,4]
output = [4,3,1,1,2,2,2]

print(frequencySort(nums))
print(output)