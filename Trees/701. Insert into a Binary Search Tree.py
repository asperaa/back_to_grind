"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""701. Insert into a Binary Search Tree [Walked through fire]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def bst_insert_helper(self, root, parent, val):
        if not root:
            if val <= parent.val:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)
            return
        if val < root.val:
            self.bst_insert_helper(root.left, root, val)
        else:
            self.bst_insert_helper(root.right, root, val)
    
    def insertIntoBST(self, root, val):
        if not root:
            return None
        self.bst_insert_helper(root, None, val)
        return root
