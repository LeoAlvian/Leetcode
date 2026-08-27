"""
981. Time Based Key-Value Store

Solved
Medium
Topics
premium lock icon
Companies

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""



# Binary Search Solutions, with time: O(1) for __init__ and set, O(logn) for get, and space: O(n)

class TimeMap:

    def __init__(self):
        self.store = {} # key: list of [val, time]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        res = ''
        if key not in self.store:
            return ''
        values = self.store[key]

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res



# Using lenear search but from the end of the array, this is a little bit faster on leetcode, if the timestamp in get(key, timestamp) is big or near the end of the array everytime then this is faster but if the array in each key is big the the binary search will be faster

class TimeMapII:

    def __init__(self):
        self.store = {} # key: list of [val, time]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        if key not in self.store:
            return ''
        values = self.store[key]

        for i in range(len(values) - 1, -1, -1):
            val, time = values[i]
            if time <= timestamp:
                return val

        return ''





ops = ["set", "get", "get", "set", "get", "get"]
args = [["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
output = [None, "bar", "bar", None, "bar2", "bar2"]

tm = TimeMap()
tm2 = TimeMapII()
res = []
res2 = []

for i in range(len(ops)):
    res.append(getattr(tm, ops[i])(*args[i]))

for i in range(len(ops)):
    res2.append(getattr(tm2, ops[i])(*args[i]))

print(res)
print(res2)
print(output)