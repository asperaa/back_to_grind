"""We are the captains of our ship, and we stay 'till the end. We see our stories through.
"""

"""104. Maximum Depth of Binary Tree [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def max_depth_helper(self, root):
        if not root:
            return 0
        l_height = 1 + self.max_depth_helper(root.left)
        r_height = 1 + self.max_depth_helper(root.right)
        return max(l_height, r_height)

    def maxDepth(self, root):
        self.max_depth_helper(root)
