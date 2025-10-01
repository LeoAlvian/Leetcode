"""
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.


Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
"""

def numWaterBottles(numBottles, numExchange):
    fullB = numBottles
    emptyB = numBottles
    res = 0

    # Loop until full bottle are less than 0
    while fullB > 0:    
        res += fullB
        # Calculate the integer division from empty bottle with numExchange and store it in 
        # fullB
        fullB = emptyB // numExchange
        # Calculate emptyB as a mod of emtpyB with numExchange to get the reminder
        emptyB = emptyB % numExchange
        # Adding emptyB with FullB 
        emptyB = emptyB + fullB
    
    return res

numBottles = 15
numExchange = 4
output = 19
nwb = numWaterBottles(numBottles, numExchange)
print(nwb)