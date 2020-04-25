"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""501. Find Mode in Binary Search Tree [T - O(n) and S - O(1) Ignore Stack Space]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    max_count = 0
    curr_count = 0
    prev = None
    result = []
    
    def findMode(self, root):
        self.dfs(root)
        return result
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.curr_count = 1 if root.val != self.prev else self.curr_count + 1
            if self.curr_count == self.max_count:
                self.result.append(root.val)
            elif self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.result = [root.val]
            self.prev = root.val
            self.dfs(root.right)