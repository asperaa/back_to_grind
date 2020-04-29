"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""951. Flip Equivalent Binary Trees [Clean]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def flipEquiv(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.flipEquiv(t1.left, t2.left) and self.flipEquiv(t1.right, t2.right) or self.flipEquiv(t1.left, t2.right) and self.flipEquiv(t1.right, t2.left)