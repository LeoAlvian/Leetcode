"""
Docstring for StoneGame

877. Stone Game

Solved
Medium
Topics
premium lock icon
Companies

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.



Example 2:
Input: piles = [3,7,2,3]
Output: true
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""

# Using Dynamic Programming
def StoneGame(piles):
    dp = {} # (l, r) -> sum of Alice Stone

    def dfs(l, r):
        if l > r :
            return 0
        if (l, r) in dp:
            return dp[(l, r)]
        
        # even variable is to determine if Alice's turn to pick, because of len(piles) are 
        # even so after alice pick the len(piles) gonna be even, so if it's odd which  
        # means it is Bob's turn to play so we not gonna include the sum to it 
        # And to determine if it is Alice turn we use even = (r - l) % 2 -> even = 1
        odd = (r - l) % 2
        left = piles[l] if odd else 0
        right = piles[r] if odd else 0
        dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)

        return dp[(l, r)]

    alice_stone = dfs(0, len(piles) - 1)
    return alice_stone > sum(piles) - alice_stone


piles = [3,7,2,3]
output = True
sg = StoneGame(piles)
print(sg)
print(output)