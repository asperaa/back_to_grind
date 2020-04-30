"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""589. N-ary Tree Preorder Traversal [Iterative]
"""

class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def preorder(self, root):
        if not root:
            return []
        stack = []
        stack.append(root)
        order = []
        while stack:
            node = stack.pop()
            order.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                if node.children[i]:
                    stack.append(node.children[i])
        return order
    
    def preorder_2(self, root):
        if not root:
            return []
        stack, order = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack.extend(node.children[::-1])
        return order 
