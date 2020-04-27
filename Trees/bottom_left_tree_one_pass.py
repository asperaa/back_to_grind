"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""513. Find Bottom Left Tree Value [One Pass]
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def findBottomLeftValue(self, root):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val