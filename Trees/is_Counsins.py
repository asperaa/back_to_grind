"""We are captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""993. Cousins in Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def parent_depth_info_dfs(self, root, x, y, depth, parent):
        if not root:
            return
        if root.val == x:
            self.x_node = root
            self.x_depth = depth
            self.x_parent = parent
        elif root.val == y:
            self.y_node = root
            self.y_depth = depth
            self.y_parent = parent
        self.parent_depth_info_dfs(root.left, x, y, depth+1, root)
        self.parent_depth_info_dfs(root.right, x, y, depth+1, root)
        

    def isCousins(self, root, x, y):
        self.x_node = None
        self.y_node = None
        self.x_parent = None
        self.y_parent = None
        self.x_depth = 0
        self.y_depth = 0
        self.parent_depth_info_dfs(root, x, y, 0, None)
        if self.x_parent != self.y_parent and self.x_depth == self.y_depth:
            return True
        return False 
