"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""513. Find Bottom Left Tree Value [Two Passes]
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def findBottomLeftValue(self, root):
        final_row = self.height(root)
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if level == final_row:
                return node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))


