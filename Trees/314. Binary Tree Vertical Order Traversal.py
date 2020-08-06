"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""314. Binary Tree Vertical Order Traversal
"""

from collections import deque, defaultdict

class Solution:

    def verticalOrder(self, root):
        if not root:
            return []
        ans = []
        queue = deque()
        table = defaultdict(list)
        queue.append((root, 0))
        minn = float('inf')
        maxx = float('-inf')
        while queue:
            node, hor_dist = queue.popleft()
            minn = min(minn, hor_dist)
            maxx = max(maxx, hor_dist)
            table[hor_dist].append(node.val)
            if node.left:
                queue.append((node.left, hor_dist-1))
            if node.right:
                queue.append((node.right, hor_dist+1))
        for i in range(minn, maxx+1):
            ans.append(table[i])
        return ans
