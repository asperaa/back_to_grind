"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""700. Search in a Binary Search Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            subtree = self.searchBST(root.left, val)
        else:
            subtree = self.searchBST(root.right, val)
        return subtree