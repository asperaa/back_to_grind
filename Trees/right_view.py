# https://leetcode.com/problems/binary-tree-right-side-view/description/


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()

                if _== level_size -1:
                    result.append(node.val) 
                
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
            