"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""637. Average of Levels in Binary Tree
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def averageOfLevels(self, root):
        average_levels = []
        queue = deque()
        queue.append(root)
        queue.append(None)
        level_nodes = 0
        level_sum = 0
        while queue:
            node = queue.popleft()
            if node:
                level_sum += node.val
                level_nodes += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                average_levels.append(level_sum / level_nodes)
                level_sum = 0
                level_nodes = 0
                if queue:
                    queue.append(None)
        return average_levels