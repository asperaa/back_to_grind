"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""222. Count Complete Tree Nodes [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def height(self, root):
        if not root:
            return 0
        return 1 + self.height(root.left)
    
    def countNodes(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height == right_height: # Left subtree is perfect BT.
            left_subtree_count_and_root = ((1 << left_height) - 1) + 1
            return left_subtree_count_and_root + self.countNodes(root.right)
        elif left_height > right_height: # Right subtree is perfect BT.
            right_subtree_count_and_root = ((1 << right_height)-1) + 1
            return right_subtree_count_and_root + self.countNodes(root.left)
