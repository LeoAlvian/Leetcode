"""
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.

Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
"""

Test1 = {'inp': {'n': 2, 'languages' : [[1],[2],[1,2]], 'friendships' : [[1,2],[1,3],[2,3]]}, 'out': 1}
Test2 = {'inp': {'n': 3, 'languages' : [[2],[1,3],[1,2],[3]], 'friendships' : [[1,4],[1,2],[3,4],[2,3]]}, 'out': 2}


class Solution:
    def minimumTeachings(self, n, languages, friendships):
        # set a people that cannot communicate, we use set so there will be no duplicate 
        cannot_com = set()

        # find people from friendships that cannot communicate with one another, if there is then adding it to cannot_com variable 
        for firstP, secondP in friendships:
            can_com = False
            can_speak = set(languages[firstP - 1])
            for lang in languages[secondP - 1]:
                if lang in can_speak:
                    can_com = True
                    break
            if not can_com:
                cannot_com.add(firstP - 1)
                cannot_com.add(secondP - 1)

        # if there is no people that cannot communicate which means we don't have to teach anyone 
        if not cannot_com:
            return 0
        
        # count how many people speak specific languages 
        # example count = [1,2,1] which means second languages are popular 
        count = [0] * n
        for person in cannot_com:
            for lang in languages[person]:
                count[lang - 1] += 1
        
        # Find the highest value of popular languages 
        max_count = 0
        for c in count:
            max_count = max(max_count, c)
        
        return len(cannot_com) - max_count




s = Solution()
res = s.minimumTeachings(Test1['inp']['n'],Test1['inp']['languages'],Test1['inp']['friendships'])
print('Test1', res == Test1['out'])
res = s.minimumTeachings(Test2['inp']['n'],Test2['inp']['languages'],Test2['inp']['friendships'])
print('Test2', res == Test2['out'])