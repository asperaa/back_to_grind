"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""590. N-ary Tree Postorder Traversal
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def postorder_helper(self, root):
        if root:
            for child in root.children:
                self.postorder_helper(child)
            self.post_order.append(root.val)

    def postorder(self, root):
        self.post_order = []
        self.postorder_helper(root)
        return self.post_order