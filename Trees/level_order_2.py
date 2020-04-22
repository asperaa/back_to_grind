"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""102. Binary Tree Level Order Traversal II
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def levelOrderBottom(self, root):
        if not root:
            return None
        levels, queue = deque(), deque()
        level = []
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                levels.appendleft(level)
                level = []
                if queue:
                    queue.append(None)
        return levels