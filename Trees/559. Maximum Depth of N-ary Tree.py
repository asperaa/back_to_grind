"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""559. Maximum Depth of N-ary Tree [Recursive]
"""

class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        max_depth = 1
        for child in root.children:
            depth = 1 + self.maxDepth(child)
            max_depth = max(max_depth, depth)
        return max_depth

