"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""222. Count Complete Tree Nodes [Iterative]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Height in Complete BT.
    def height(self, root):
        if not root:
            return 0
        return 1 + self.height(root.left)
    
    def countNodes(self, root):
        if not root:
            return 0
        count = 0
        while root:
            left_subtree_height = self.height(root.left)
            right_subtree_height = self.height(root.right)
            if left_subtree_height == right_subtree_height: # Left subtree is perfect binary tree.
                left_subtree_count = (1 << left_subtree_height) - 1 # [Formaula - 2**h - 1]
                left_subtree_count_and_root = left_subtree_count + 1
                count += left_subtree_count_and_root
                root = root.right # Explore the right subtree.
            elif left_subtree_height > right_subtree_height: # Right subtree is perfect binary tree.
                right_subtree_count = (1 << right_subtree_height) - 1
                right_subtree_count_and_root = right_subtree_count + 1
                count += right_subtree_count_and_root
                root = root.left # Explore the left subtree.
        return count


