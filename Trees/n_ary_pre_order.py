"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""589. N-ary Tree Preorder Traversal
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def preorder_helper(self, root):
        if root:
            self.pre_order.append(root.val)
            for child in root.children:
                self.preorder_helper(child)
    
    def preorder(self, root):
        self.pre_order = []
        self.preorder_helper(root)
        return self.pre_order

    