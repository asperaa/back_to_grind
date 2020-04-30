"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""429. N-ary Tree Level Order Traversal [Iterative]
"""

from collections import deque

class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def levelOrder(self, root):
        if not root:
            return []
        levels, level = [], []
        queue = deque()
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if node:
                level.append(node.val)
                for child in node.children:
                    if child:
                        queue.append(child)
            else:
                levels.append(level)
                level = []
                if queue:
                    queue.append(None)
        return levels