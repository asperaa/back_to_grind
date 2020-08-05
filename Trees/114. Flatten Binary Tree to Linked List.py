"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""114. Flatten Binary Tree to Linked List
"""

class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root
