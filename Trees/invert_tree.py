"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""226. Invert Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def invertTree(self, root):
        if not root:
            return None
        left_subtree = root.left
        root.left = root.right
        root.right = left_subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root