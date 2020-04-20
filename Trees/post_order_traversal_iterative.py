"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""145. Binary Tree Postorder Traversal [Iterative]
"""

class Solution:

    def push_left_nodes(self, root, stack):
        while root:
            stack.append((root, False))
            root = root.left
    
    def postorderTraversal(self, root):
        if not root:
            return []
        result, stack = []
        self.push_left_nodes(root, stack)
        while stack:
            node, visited_right_subtree = stack.pop()
            if visited_right_subtree:
                result.append(node.val)
            else:
                stack.append(node, True)
                self.push_left_nodes(node.right, stack)
        return result
