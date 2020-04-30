"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""559. Maximum Depth of N-ary Tree [Iterative]
"""

from collections import deque

class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        max_depth = 0
        while stack:
            node, level = stack.pop()
            max_depth = max(max_depth, level)
            if node:
                for child in node.children:
                    stack.append((node, level+1))
        return max_depth
