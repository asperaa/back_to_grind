"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

from collections import deque

class Solution:

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        sub_result = []
        queue = deque()
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if node:
                sub_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(sub_result)
                if queue:
                    sub_result = []
                    queue.append(None)
        return result

