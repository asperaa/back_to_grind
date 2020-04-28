"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""965. Univalued Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, value):
        if not root:
            return True
        left_unival = self.dfs(root.left, value)
        right_unival = self.dfs(root.right, value)
        if root.val != value:
            return False
        return left_unival and right_unival
    
    def isUnivalTree(self, root):
        if not root:
            return True
        return self.dfs(root, root.val)
