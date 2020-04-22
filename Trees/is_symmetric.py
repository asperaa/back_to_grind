"""We are the captains of our ships and we stay 'till the end. We see our stories through.
"""

"""101. Symmetric Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def is_symmetric_helper(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        left_symmetric = self.is_symmetric_helper(t1.left, t2.right)
        right_symmetric = self.is_symmetric_helper(t1.right, t2.left)
        return left_symmetric and right_symmetric
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.is_symmetric_helper(root.left, root.right)