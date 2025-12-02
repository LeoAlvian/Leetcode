"""
1325. Delete Leaves With a Given Value

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 
Example 1:

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).



Example 2:

Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]



Example 3:

Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deleteLeavesValue(root, target):
    if not root:
        return None
    
    root.left = deleteLeavesValue(root.left, target)
    root.right = deleteLeavesValue(root.right, target)

    if not root.left and not root.right and root.val == target:
        return None
    
    return root

def printTreeLevelbyLevel(root):
    if not root:
        return
    
    queue = deque([root])
    print('queue', queue)

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level = []

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(str(node.val))

            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            
        
        # Print the current level on a single line
        print(" ".join(current_level))
    

#            [1]
#         /       \
#       [3]       [3]
#     /     \   
#   [3]    [2]     
arr = [1,3,3,3,2]
target = 2
output = [1,3,None,None,2]

root = Node(1)
root.left = Node(3)
root.right = Node(3)
root.left.left = Node(3)
root.left.right = Node(2)

dlv = deleteLeavesValue(root, target)
printTreeLevelbyLevel(dlv)
print(output)