"""
41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.



Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.


Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1


Solution 2 - 3 loops
Conceptual Approach to Finding the First Missing Positive Integer
When faced with the problem of finding the first missing positive integer in an unsorted array, it's crucial to adopt a strategy that efficiently uses both time and space. At first glance, this problem might seem to require sorting the array or using additional memory, but in reality, a more elegant solution exists that operates in linear time and constant space.

Let`s walk through this approach using the input [3, 4, -1, 1].

Core Idea
The key insight for this problem is that we can use the original array itself to track the presence of positive integers in the range [1, len(nums)].
By marking certain indices as negative, we can encode the presence of each number without using extra space.



Step 1: 
Clean the Array
Since we only care about integers between 1 and len(nums),
we first replace all irrelevant values (e.g., negatives, zeros, and numbers greater than len(nums)) in-place with a dummy value (e.g., n + 1), which cannot affect our logic.

For example, starting with [3, 4, -1, 1]:

-1 is not relevant.
All values > 4 (i.e., len(nums)) are also irrelevant.
We transform it to: [3, 4, 5, 1]
(Note: The actual dummy value used is n + 1 = 5, which is out of bounds.)



Step 2:
Mark the Presence of Values
Next, we iterate through the array again.
For each number num in the array, if 1 <= abs(num) <= n, we use its value to mark the index abs(num) - 1 by making the number at that index negative (only if it’s not already negative).

This marking shows that num exists in the array.

Example:
From [3, 4, 5, 1], we mark:

3 → index 2 → mark as negative: [3, 4, -5, 1]
4 → index 3 → mark as negative: [3, 4, -5, -1]
-5 (was 5) → skip (out of range)
-1 (was 1) → index 0 → mark as negative: [-3, 4, -5, -1]



Step 3: 
Find the First Missing Positive
Finally, we scan the array from index 0 to n-1.
The first index i where nums[i] is positive tells us that i + 1 is missing.

In our example: [-3, 4, -5, -1]
The value at index 1 is still positive → the first missing positive is 2.

If all indices are negative, it means all numbers from 1 to n exist, so the answer is n + 1.

Why This Works
This method treats the input array as a kind of hash set:
we use signs (positive/negative) to mark whether a number exists in the array.

Time Complexity: O(n) — each operation (replace, mark, check) is linear
Space Complexity: O(1) — we don't use any extra space beyond the input array
Conclusion
This algorithm efficiently finds the first missing positive integer in three steps:

Clean irrelevant values in-place
Mark presence using index negation
Scan to find the first positive index
By using the array itself as a tracking mechanism, we avoid extra space and achieve optimal performance.

Complexity
Time complexity: O(n)
Space complexity: O(1)
"""

def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1



nums = [3,4,-1,1]
output = 2
fmp = firstMissingPositive(nums)
print(fmp)
print(output)