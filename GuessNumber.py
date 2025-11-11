"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

 -1: Your guess is higher than the number I picked (i.e. num > pick).
  1: Your guess is lower than the number I picked (i.e. num < pick).
  0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:
Input: n = 10, pick = 6
Output: 6


Example 2:
Input: n = 1, pick = 1
Output: 1


Example 3:
Input: n = 2, pick = 1
Output: 1
"""



# Using Binary search to optimize time complexity to O(logn)
# guess API that return 0 if the guess are correct, -1 if it's too high or 1 if it's 
# too low
def guess(n):
    pick = 16
    if n == pick:
        return 0
    elif n > pick:
        return -1
    else:
        return 1


def guessNum(n):
    l, r = 1, n

    while l <= r:
        mid = (l + r) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            r = mid - 1
        else:
            l = mid + 1

n = 20
output = 16
gn = guessNum(n)
print(gn)
print(output)