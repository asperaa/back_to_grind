"""We are the captains of our ships, and we stay 'till the end. We see our stories through. 
"""

"""100. Same Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def isSameTree(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        if not root_1 or not root_2:
            return False
        if root_1.val != root_2.val:
            return False
        left_same = self.isSameTree(root_1.left, root_2.left)
        right_same = self.isSameTree(root_1.right, root_2.right)
        return left_same and right_same