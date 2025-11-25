"""
895. Maximum Frequency Stack

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""


# We gonna use three variable to keep track of max count, count of each number and 
# stacks of list of each number in relation to it's count
#
# Ex
#
# [5, 7, 5, 7, 4, 5]
# maxC = 3 because 5 appear 3 times
# count = {5:3, 7:2, 4:1}  -> how many times the number appears
# stacks = { cnt | Group
#             1:  [5,7,4]
#             2:  [5,7]     -> we need to add in sequence so when we pop it we gonna 
#             3:  [5]          pop it from the top
#          }
# If we pop all element it's gonna be like this
# output = [5, 7, 5, 4, 7, 5]

class FreqStack:
    def __init__(self):
        self.cnt = {}
        self.maxC = 0
        self.stacks = {}
    
    def push(self, val):
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt > self.maxC:
            self.maxC = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)
    
    def pop(self):
        res = self.stacks[self.maxC].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxC]:
            del self.stacks[self.maxC]
            self.maxC -= 1
        return res


ops = ["push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
args = [[5], [7], [5], [7], [4], [5], [], [], [], []]
output = [None, None, None, None, None, None, 5, 7, 5, 4]
fs = FreqStack()
res = []
for i in range(len(ops)):
    res.append(getattr(fs, ops[i])(*args[i]))
print(res)
print(output)