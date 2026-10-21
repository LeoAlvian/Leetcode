"""
1079. Letter Tile Possibilities
Solved
Medium
Topics
premium lock icon
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".



Example 2:

Input: tiles = "AAABBC"
Output: 188



Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""


from collections import Counter
# Solving it using backtrack with time: O(2^n) or worse O(n!), space: O(2^n)
def numTilePossibilities(tiles):
    count = Counter(tiles)

    def backtrack():
        res = 0

        for c in count:
            if count[c] > 0:
                count[c] -= 1
                res += 1
                res += backtrack()
                count[c] += 1

        return res

    return backtrack()



tiles = "AAABBC"
output = 188 

res = numTilePossibilities(tiles)

print(res)
print(output)