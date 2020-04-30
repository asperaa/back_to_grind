"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""590. N-ary Tree Postorder Traversal [Iterative]
"""

class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def postorder(self, root):
        if not root:
            return []
        stack, order = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack.extend(node.children)
        return order[::-1]