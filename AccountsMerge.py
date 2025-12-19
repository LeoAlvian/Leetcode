"""
Docstring for AccountsMerge

721. Accounts Merge

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.



Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

# Using Union Find or Disjoint Set Union (DSU) algorithm
# Usage:
# 1. Detect cycle in a graph
# 2. Check network connectivity
# 3. Minimum spanning tree(Kruskal's Algorithm) 
#
# Union Find is a data structure for managing disjoint sets
# benefit:
# 1. Quickly determine if two elements belong to the same set
# 2. Quickly merge two sets
#
# Union Find Main operation
# 1. Create set -> Create a new set for each element
# 2. Find       -> Find the representative(root node) of the set
# 3. Union      -> Merge two sets
#
# Ex:
#
# n = 4
# Union Create a set -> making each val to be their own parent
# val = [0, 1, 2, 3]
# idx = [0, 1, 2, 3]
#
# union(0,1)          -> making 0 a parent of 1 by setting value on index 1 to be 
#                        the val idx of 0 which is 0
# val = [0, 0, 2, 3]
# idx = [0, 1, 2, 3]
#
# union(1,2)          -> making 1 a parent of 2 by setting value on index 2 to be 
#                        the val idx of 1 which is 0
# val = [0, 0, 0, 3]
# idx = [0, 1, 2, 3]


from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        if self.size[px] > self.size[py]:
            self.parent[py] = px
            self.size[px] += 1
        else:
            self.parent[px] = py
            self.size[py] += 1
        return


class Solution:
    def mergeAcc(self, accounts):
        uf = UnionFind(len(accounts))
        emailToAccIdx = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAccIdx:
                    uf.union(i, emailToAccIdx[email])
                else:
                    emailToAccIdx[email] = i
        
        emailGroup = defaultdict(list)
        for email, i in emailToAccIdx.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res


accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
    ]
output = [
    ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
    ]

s = Solution()
res = s.mergeAcc(accounts)
print(res)
print(output)