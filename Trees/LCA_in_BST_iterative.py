"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""235. Lowest Common Ancestor of a Binary Search Tree [Iterative]. T - O(n) and S - O(1).
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root, x, y):
        while root:
            if x.val < root.val and y.val < root.val:
                root = root.left
            elif x.val > root.val and y.val > root.val:
                root = root.right
            else:
                break
        return root