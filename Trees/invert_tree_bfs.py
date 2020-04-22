"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""100. Same Tree
"""
from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def invertTree(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            left_subtree = node.left
            node.left = node.right
            node.right = left_subtree
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root