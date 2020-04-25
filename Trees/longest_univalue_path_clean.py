"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""687. Longest Univalue Path
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root):
        if not root:
            return 0
        left_length = self.dfs(root.left)
        right_length = self.dfs(root.right)
        left_arrow = right_arrow = 0
        if root.left and root.left.val == root.val:
            left_arrow = left_length + 1
        if root.right and root.right.val == root.val:
            right_arrow = right_length + 1
        self.ans = max(self.max, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    def longestUnivaluePath(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans