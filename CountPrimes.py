"""
204. Count Primes

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.



Example 2:

Input: n = 30
output = 10
Explanation: There are 10 prime numbers less than 30, they are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29



Example 2:

Input: n = 0
Output: 0



Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""

# We Gonna solve this using Sieve of Eratosthenes
"""
Sieve of Eratosthenes
Intuition
Instead of checking each number for primality, we can use the Sieve of Eratosthenes to efficiently mark composite numbers. The key insight is that when we find a prime number, all of its multiples must be composite. By marking these multiples, we eliminate the need to check them later. We start marking from the square of each prime because smaller multiples would have already been marked by smaller primes.

Algorithm
1. Create a boolean array sieve of size n, initialized to false (all numbers assumed prime).
2. Initialize a counter res to 0.
3. For each number from 2 to n-1:
    If the number is not marked as composite (sieve[num] is false):
        Increment the prime counter.
        Mark all multiples of this number starting from num*num as composite.
4. Return the count of primes.
"""



def countPrimes(n):
    sieve = [False] * n
    res = 0

    for num in range(2, n):
        if not sieve[num]:
            res += 1
            for i in range(num * num, n, num):
                sieve[i] = True
    
    return res


n = 30
output = 10

res = countPrimes(n)

print(res)
print(output)