"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""111. Minimum Depth of Binary Tree [Iterative]
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def minDepth(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            else:
                self.minDepth(root.left, level+1)
                self.minDepth(root.right, level+1)
