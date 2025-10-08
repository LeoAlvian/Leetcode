"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


class SortArr:
    def sorta(self, nums):

        # Merge back the individual element into a single arr
        def merge(arr, L, M, R):
            # Creating left array and right array and also creating apointer for 
            # one result array pointer, left and right pointer 
            leftArr, rightArr = arr[L:M+1], arr[M+1:R+1]
            arrP, Lp, Rp = L, 0, 0

            # Loop throught it and check if left arr is less or equal to right arr
            # if it is the we put left arr to the result arr else we put the right arr
            while Lp < len(leftArr) and Rp < len(rightArr):
                if leftArr[Lp] <= rightArr[Rp]:
                    arr[arrP] = leftArr[Lp]
                    Lp += 1
                else:
                    arr[arrP] = rightArr[Rp]
                    Rp += 1
                arrP += 1
            
            # There will be a left over after we put both left and right arr together
            # To accomodate that we loop throught left or right arr and put it into 
            # result array
            while Lp < len(leftArr):
                nums[arrP] = leftArr[Lp]
                Lp += 1
                arrP += 1
            
            while Rp < len(rightArr):
                nums[arrP] = rightArr[Rp]
                Rp += 1
                arrP += 1


        # Using recursive mergeSort methods
        def mergeSort(arr, L, R):
            if L == R:
                return arr
            
            # We spliting the arr into two recursively and then merge them after
            # we get into an individual element of the arr
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M + 1, R)
            merge(arr, L, M, R)

            return arr

        # This is the first code that gonna be execute, which is calling mergeSort
        # recursive methods
        return mergeSort(nums, 0, len(nums) - 1)


nums = [5,1,1,2,0,0]
output = [0,0,1,1,2,5]

sa = SortArr()
print(sa.sorta(nums))
print(output)