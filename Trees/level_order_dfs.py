"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""102. Binary Tree Level Order Traversal [DFS]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs_helper(self, root, levels, level):
        if not root:
            return
        if len(levels) < level + 1:
            levels.append([])
        levels[level].append(root.val)
        self.dfs_helper(root.left, levels, level+1)
        self.dfs_helper(root.right, levels, level+1)
    
    def levelOrder(self, root):
        levels = []
        self.dfs_helper(root, levels, 0)
        return levels