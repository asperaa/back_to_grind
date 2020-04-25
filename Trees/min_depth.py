"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""111. Minimum Depth of Binary Tree [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def minDepth(self, root):
        if not root:
            return 0
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))