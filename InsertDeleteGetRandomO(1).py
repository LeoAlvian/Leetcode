"""
380. Insert Delete GetRandom O(1)

Solved
Medium
Topics
premium lock icon
Companies

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""


# numMap = {1:0, 2:1}
# numList = [1, 2]
#
# remove(1)
# idx = numMap[1] => 0
# lastVal = numList[-1] => 2
#
# Set numList[index] to be the last value
# numList[0] = 1
# numList = [2, 2]
# Set numMap[lastValue] to the index
# numMap[2] = 0
# numMap = {1:0, 2:0}
#
# Deleting the value from list
# numList.pop()
# numList = [2]
# Deleting the value from numMap
# del numMap[1]
# numMap = {2:0}


import random

class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val):
        if val in self.numMap:
            return False
        
        self.numMap[val] = len(self.numList)
        self.numList.append(val)

        return True

    def remove(self, val):
        if val not in self.numMap:
            return False
        
        # Get index of the value we gonna delete from numMap
        # Get the last value from numList
        idx = self.numMap[val]
        lastVal = self.numList[-1]

        # Set numList[index] to be the last value
        # Set numMap[lastValue] to the index
        self.numList[idx] = lastVal
        self.numMap[lastVal] = idx

        # Deleting the value from list
        # Deleting the value from numMap
        self.numList.pop()
        del self.numMap[val]

        return True

    def getRandom(self):
        return random.choice(self.numList)


ops = ["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
args = [[1], [2], [2], [], [1], [2], []]
output = [True, False, True, 2, True, False, 2]


rs = RandomizedSet()
res = []
for i in range(len(ops)):
    res.append(getattr(rs, ops[i])(*args[i]))

print(res)
print(output)