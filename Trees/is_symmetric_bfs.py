"""We are captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""101. Symmetric Tree [Iterative]
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def isSymmetric(self, root):
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True