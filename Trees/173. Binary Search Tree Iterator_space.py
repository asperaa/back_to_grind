"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""173. Binary Search Tree Iterator [T - Oh(1) and S - O(logn)]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.explore_left_subtree(root)

    def explore_left_subtree(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self):
        next_smallest = self.stack.pop()
        self.explore_left_subtree(next_smallest.right)
        return next_smallest.val
    
    def hasNext(self):
        return len(self.stack) != 0

            