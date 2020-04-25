"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""235. Lowest Common Ancestor of a Binary Search Tree [Recursive] T - O(h) and S - O(h) 
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def lca_helper(self, root, x, y):
        if x > root.val and y > root.val:
            self.lca_helper(root.left, x, y)
        elif x < root.val and y < root.val:
            self.lca_helper(root.right, x, y)
        else:
            self.lca = root
            return
    
    def lowestCommonAncestor(self, root, x, y):
        self.lca = None
        self.lca_helper(root, x, y)
        return self.lca