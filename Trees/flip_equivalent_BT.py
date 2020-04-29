"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""951. Flip Equivalent Binary Trees [Walked through Fire]
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
        if not t1.left or not t1.right:
            if not t1.left and not t2.left and not t1.right and not t2.right:
                return True
            elif t1.left and t2.left and t1.left.val == t2.left.val:
                left_flip = self.flipEquiv(t1.left, t2.left)
                right_flip = self.flipEquiv(t1.right, t2.right)
            elif t1.right and t2.right and t1.right.val == t2.right.val:
                left_flip = self.flipEquiv(t1.left, t2.left)
                right_flip = self.flipEquiv(t1.right, t2.right)
            elif t1.left and t2.right and t1.left.val == t2.right.val:
                left_flip = self.flipEquiv(t1.left, t2.right)
                right_flip = self.flipEquiv(t1.right, t2.left)
            elif t1.right and t2.left and t1.right.val == t2.left.val:
                left_flip = self.flipEquiv(t1.left, t2.right)
                right_flip = self.flipEquiv(t1.right, t2.left)
            else:
                return False
        elif t1.left and t1.right and t2.left and t2.right:
            if t1.left.val == t2.left.val and t1.right.val == t2.right.val:
                left_flip = self.flipEquiv(t1.left, t2.left)
                right_flip = self.flipEquiv(t1.right, t2.right)
            elif t1.left.val == t2.right.val and t1.right.val == t2.left.val:
                left_flip = self.flipEquiv(t1.left, t2.right)
                right_flip = self.flipEquiv(t1.right, t2.left)
            else:
                return False
        else:
            return False
        return left_flip and right_flip