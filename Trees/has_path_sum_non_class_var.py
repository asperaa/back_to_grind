"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""112. Path Sum [No Class Variable Use]
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def hasPathSum(self, root, summ):
        if not root:
            return False
        if not root.left and not root.right:
            summ -= root.val
            return summ == 0
        return self.hasPathSum(root.left, summ - root.val) or self.hasPathSum(root.right, summ - root.val)