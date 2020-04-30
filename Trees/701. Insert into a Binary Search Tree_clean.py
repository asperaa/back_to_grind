"""We are the captains of our ships and we stay 'till the end. We see our stories through.
"""

"""701. Insert into a Binary Search Tree [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root