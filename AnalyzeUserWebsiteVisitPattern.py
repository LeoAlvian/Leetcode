"""
Analyze User Website Visit Pattern

Medium
Topics
Company Tags

You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple (username[i], website[i], timestamp[i]) indicates that the user username[i] visited the website website[i] at time timestamp[i].

A list of three websites is called a pattern (not neccessarily distinct).

For example, ["neetcode", "courses", "problems"], ["neetcode", "love", "neetcode"], and ["dsa", "dsa", "dsa] are all patterns.
The score of a pattern is the number of users visited all the websites in the pattern in the same order they appeared in the pattern. In other words, for a given users' sequence of website visits, the pattern must appear as a subsequence within that sequence.

Your task is to return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.



Example 1:
Input: username = ["bob","bob","bob","alice","alice","alice","alice","charlie","charlie","charlie"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]



Example 2:
Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]



Constraints:

1 <= username.length == timestamp.length == website.length <= 50
1 <= username[i].length <= 10
1 <= timestamp[i] <= 1,000,000,000
1 <= website[i].length <= 10
username[i] and website[i] is made up of lowercase English letters.
It is guaranteed that there is at least one user who visited at least three websites.
All the tuples (username[i], timestamp[i], website[i]) are unique.
"""


from collections import defaultdict

def mostVisitedPattern(username, timestamp, website):
    # Sort all visits by timestamp to ensure chronological order.
    arr = list(zip(timestamp, username, website))
    arr.sort(key = lambda x : x[0])
    # arr = [(1, 'bob', 'home'), (2, 'bob', 'about'), (3, 'bob', 'career'), (4, 'alice', 'home'), (5, 'alice', 'cart'), (6, 'alice', 'maps'), (7, 'alice', 'home'), (8, 'charlie', 'home'), (9, 'charlie', 'about'), (10, 'charlie', 'career')]


    # Group websites by user, maintaining the order of visits.
    userWebMap = defaultdict(list)
    for time, user, web in arr:
        userWebMap[user].append(web)
    # userWebMap = defaultdict(<class 'list'>, {'bob': ['home', 'about', 'career'], 'alice': ['home', 'cart', 'maps', 'home'], 'charlie': ['home', 'about', 'career']})
    

    # For each user, generate all possible 3-website patterns using three nested loops 
    # i, j, k. Store patterns in a set to avoid counting duplicates from the same user.
    count = defaultdict(int)
    for user in userWebMap:
        pattern = set()
        web = userWebMap[user]
        for i in range(len(web)):
            for j in range(i + 1, len(web)):
                for k in range(j + 1, len(web)):
                    pattern.add((web[i], web[j], web[k]))
        
        # Count how many users have each pattern.
        for p in pattern:
            count[p] += 1
    # count = defaultdict(<class 'int'>, {('home', 'about', 'career'): 2, ('home', 'cart', 'home'): 1, ('cart', 'maps', 'home'): 1, ('home', 'cart', 'maps'): 1, ('home', 'maps', 'home'): 1})
    

    # Return the pattern with the highest count, breaking ties lexicographically.
    max_count = 0
    res = tuple()
    for pattern in count:
        if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
            max_count = count[pattern]
            res = pattern
    # res = ('home', 'about', 'career')
    
    return list(res)


username = ["bob","bob","bob","alice","alice","alice","alice","charlie","charlie","charlie"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
output = ["home","about","career"]

print(mostVisitedPattern(username, timestamp, website))
print(output)