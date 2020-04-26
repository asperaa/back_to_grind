"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""572. Subtree of Another Tree. T - O(mn) and S - O(n) 
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def is_same_tree(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)
    
    def sub_tree_helper(self, t1, t2):
        if not t1 or not t2:
            return
        if t1.val == t2.val:
            self.sub_tree = self.sub_tree or self.is_same_tree(t1, t2)
        self.sub_tree_helper(t1.left, t2)
        self.sub_tree_helper(t1.right, t2)

    def isSubTree(self, t1, t2):
        self.sub_tree = False
        self.sub_tree_helper(t1, t2)
        return self.sub_tree
