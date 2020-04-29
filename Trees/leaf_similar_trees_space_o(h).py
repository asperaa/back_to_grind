"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""872. Leaf-Similar Trees [T - O(n) and S - O(h)]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, stack):
        while True:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if not node.left and not node.right:
                return node.val
    
    def leafSimilar(self, t1, t2):
        stack_1, stack_2 = [], []
        stack_1.append(t1)
        stack_2.append(t2)
        while stack_1 and stack_2:
            if self.dfs(stack_1) != self.dfs(stack_2):
                return False
        is_stack_1_empty = len(stack_1) == 0
        is_stack_2_empty = len(stack_2) == 0
        return is_stack_1_empty and is_stack_2_empty