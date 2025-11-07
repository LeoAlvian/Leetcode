"""
901. Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 

Constraints:

1 <= price <= 105
At most 104 calls will be made to next.
"""


# Using stack data structure
# We need to compare the price with every previous price that is lower or equal but
# we don't really need to check all because we gonna use stack and store pair of price
# and span of previous stock, if the are smaller or equal we add span and pop previous # price from stack keep doing it until the previous stock are larger and 
# we add it to stack and then return span
# Ex
# [100, 80, 60, 70, 60, 75, 85]
# [  1,  1,  1,  2,  1,  4,  6]
# 
#   i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1)]
# [  1,  1,  1,  2,  1,  4,  6]
#
#        i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(80,1)]
# [  1,  1,  1,  2,  1,  4,  6]
#
#            i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(80,1),(60,1)]
# [  1,  1,  1,  2,  1,  4,  6]
#
#                i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(80,1),(70,2)]
# [  1,  1,  1,  2,  1,  4,  6]  -> because 60 is <= 70, we add span and 80 > so we
# push 70 with span of 2 to the stack
#
#                    i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(80,1),(70,2),(60,1)]
# [  1,  1,  1,  2,  1,  4,  6]  
#
#                        i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(80,1),(75,4)]
# [  1,  1,  1,  2,  1,  4,  6]  -> because 60,70 is <= 75, we keep adding span until
# previous price is bigger which is 80, push 75 with span of 4 to the stack
#
#                            i
# [100, 80, 60, 70, 60, 75, 85]  -> stack = [(100,1),(85,6)]
# [  1,  1,  1,  2,  1,  4,  6]  -> because 75,80 is <= 85, we keep adding span until
# previous price is bigger which is 100, push 85 with span of 6 to the stack

class StockSpan:

    def __init__(self):
        self.stack = [] # store a pair of (price, span)

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, span))
        return span


ops = ["next", "next", "next", "next", "next", "next", "next"]
args = [[100], [80], [60], [70], [60], [75], [85]]
output = [1, 1, 1, 2, 1, 4, 6]

ss = StockSpan()
res = []
for i in range(len(ops)):
    res.append(getattr(ss, ops[i])(*args[i]))

print(res)
print(output)