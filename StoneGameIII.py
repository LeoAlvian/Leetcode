"""
1406. Stone Game III

Solved
Hard
Topics
premium lock icon
Companies
Hint

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

 

Example 1:
Input: stoneValue = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.


Example 2:
Input: stoneValue = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.



Example 3:
Input: stoneValue = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
 

Constraints:

1 <= stoneValue.length <= 5 * 104
-1000 <= stoneValue[i] <= 1000
"""


def stoneGameIII(sv):
    n = len(sv)
    dp = [0] * 4

    for i in range(n - 1, -1, -1):
        # First iteration
        # i = 3
        total = 0
        dp[i % 4] = float('-inf')
        # dp[i%4] = [0, 0, 0, -inf]
        for j in range(i, min(i + 3, n)):
            total += sv[j]
            # j = 3, stoneVal = -9
            dp[i % 4] = max(dp[i % 4], total + dp[(j + 1) % 4])
            # total - dp[(j + 1) % 4] = -9 - 0
            # max(-inf , -9) = -9
        # dp[i%4] = [0, 0, 0, -9]
    
    if dp[0] == 0:
        return 'Tie'
    return 'Alice' if dp[0] > 0 else 'Bob'


# All the iteration play out like this
# First iteration
# i 3
# dp[i%4] [0, 0, 0, -inf]
# j 3 stoneVal -9
# total - dp[(j + 1) % 4] = -9 - 0
# max -inf , -9  = -9
# dp[i%4] after [0, 0, 0, -9]
#
# Second Iteration
# i 2
# dp[i%4] [0, 0, -inf, -9]
# j 2 stoneVal 3
# total - dp[(j + 1) % 4] = 3 - -9
# max -inf , 12  = 12
# j 3 stoneVal -9
# total - dp[(j + 1) % 4] = -6 - 0
# max 12 , -6  = 12
# dp[i%4] after [0, 0, 12, -9]
#
# Third Iteration
# i 1
# dp[i%4] [0, -inf, 12, -9]
# j 1 stoneVal 2
# total - dp[(j + 1) % 4] = 2 - 12
# max -inf , -10  = -10
# j 2 stoneVal 3
# total - dp[(j + 1) % 4] = 5 - -9
# max -10 , 14  = 14
# j 3 stoneVal -9
# total - dp[(j + 1) % 4] = -4 - 0
# max 14 , -4  = 14
# dp[i%4] after [0, 14, 12, -9]
#
# Forth Iteration
# i 0
# dp[i%4] [-inf, 14, 12, -9]
# j 0 stoneVal 1
# total - dp[(j + 1) % 4] = 1 - 14
# max -inf , -13  = -13
# j 1 stoneVal 2
# total - dp[(j + 1) % 4] = 3 - 12
# max -13 , -9  = -9
# j 2 stoneVal 3
# total - dp[(j + 1) % 4] = 6 - -9
# max -9 , 15  = 15
# dp[i%4] after [15, 14, 12, -9]
# return Tie if dp[0] == 0, Alice if dp[0] > 0 else Bob



stoneValue = [1,2,3,-9]
output = "Alice"

sg = stoneGameIII(stoneValue)

print(sg)
print(output)