"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""617. Merge Two Binary Trees
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
