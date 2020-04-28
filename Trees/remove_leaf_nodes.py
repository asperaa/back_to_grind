"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1325. Delete Leaves With a Given Value
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def removeLeafNodes(self, root, value):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, value)
        root.right = self.removeLeafNodes(root.right, value)
        if not root.left and not root.right and root.val == value:
            return None
        return root