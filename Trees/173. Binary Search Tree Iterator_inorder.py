"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""173. Binary Search Tree Iterator [T - O(1), S - O(h)]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.sorted_node_values = []
        self.inorder(root)
        self.curr_index = -1
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.sorted_node_values.append(root.val)
            self.inorder(root.right)
    
    def next(self):
        self.curr_index += 1
        return self.sorted_node_values[self.curr_index]
    
    def hasNext(self):
        return self.curr_index < len(self.sorted_node_values) - 1