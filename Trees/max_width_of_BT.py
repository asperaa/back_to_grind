# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0

        queue = deque()
        queue.append((root, 0))

        while queue:

            level_size = len(queue)
            _, level_start = queue[0]
    
            for i in range(level_size):

                node, position = queue.popleft()

                if node.left:
                    queue.append((node.left, 2*position))
                if node.right:
                    queue.append((node.right, 2*position + 1))

                max_width = max(max_width, position - level_start + 1)
        return max_width   