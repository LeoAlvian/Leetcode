"""
347. Top K Frequent Elements

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]



Example 2:
Input: nums = [1], k = 1
Output: [1]



Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


def topKFrequentElements(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    # print(f'freq = {freq}')
    # nums = [1,2,1,2,1,2,3,1,3,2] -> len(nums) = 10
    #          0    1    2    3    4    5    6    7    8    9    10
    # freq = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [  ]]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # print(f'count = {count}')
    # count = {1: 4, 2: 4, 3: 2}

    for n, c in count.items():
        freq[c].append(n)
    # print(f'freq2 = {freq}')
    # Map the number of appearance to the list of nums
    #           0    1    2    3     4      5    6    7    8    9    10
    # freq2 = [[ ], [ ], [3], [ ], [1, 2], [ ], [ ], [ ], [ ], [ ], [  ]]
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for el in freq[i]:
            res.append(el)
            # print(f'res = {res}')
            # res = [1, 2]
            if len(res) == k:
                return res


nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
output = [1,2]

tkf = topKFrequentElements(nums, k)

print(tkf)
print(output)