"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""515. Find Largest Value in Each Tree Row
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def largestValues(self, root):
        if not root:
            return []
        largest_values = []
        queue = deque()
        queue.append(root)
        queue.append(None)
        row_max = float('-inf')
        while queue:
            node = queue.popleft()
            if node:
                row_max = max(row_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                largest_values.append(row_max)
                row_max = float('-inf')
                if queue:
                    queue.append(None)
        return largest_values
