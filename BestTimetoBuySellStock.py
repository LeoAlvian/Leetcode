"""
121. Best Time to Buy and Sell Stock

Solved
Easy
Topics
premium lock icon
Companies

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

# Two pointer technique
def bestTimeBuySellStock(prices):
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r += 1
    
    return maxProfit


# Using maxProfit and minPrice
def bestTimeBuySellStockII(prices):
    minPrice = prices[0]
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        profit = price - minPrice
        if profit > maxProfit:
            maxProfit = profit
    
    return maxProfit

prices = [7,1,5,3,6,4]
output = 5

bt = bestTimeBuySellStock(prices)
bt2 = bestTimeBuySellStockII(prices)

print(bt)
print(bt2)
print(output)