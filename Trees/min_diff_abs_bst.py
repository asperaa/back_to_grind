"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""530. Minimum Absolute Difference in BST
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            curr_diff = root.val - self.prev
            self.result = min(self.result, curr_diff)
            self.prev = root.val
            self.dfs(root.right)

    def getMinimumDifference(self, root):
        self.result = float('inf')
        self.prev = float('-inf')
        self.dfs(root)
        return self.result