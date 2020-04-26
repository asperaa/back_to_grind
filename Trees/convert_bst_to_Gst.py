"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1038. Binary Search Tree to Greater Sum Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def bst_to_gst_helper(self, root):
        if not root:
            return None
        self.bst_to_gst_helper(root.right)
        self.total += root.val
        root.val = self.total
        self.bst_to_gst_helper(root.left)
        return root
    
    def bstToGst(self, root):
        self.total = 0
        return self.bst_to_gst_helper(root)