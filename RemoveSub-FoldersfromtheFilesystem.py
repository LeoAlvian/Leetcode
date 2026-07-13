"""
1233. Remove Sub-Folders from the Filesystem

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.



Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".



Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
"""



# Solving Using Prefix Tree or Trie(more technical term) with time complexity is O(n * m) 
# and space: O(n * m) where n is the size of the array folders and m is the length of each 
# string

class Trie:

    def __init__(self):
        self.children = {}
        self.end_of_folder = False
        
    def add(self, path):
        cur = self
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True
    
    def prefix_search(self, path):
        cur = self
        folders = path.split('/')
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False

class Solution: 

    def removeSubfolders(self, folders):
        trie = Trie()
        for f in folders:
            trie.add(f)
        res = []
        for f in folders:
            if not trie.prefix_search(f):
                res.append(f)
        return res



folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
output = ["/a","/c/d","/c/f"]

s = Solution()

res = s.removeSubfolders(folders)

print(res)
print(output)