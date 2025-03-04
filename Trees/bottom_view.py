# https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

#User function Template for python3
from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return []
            
        bottom_view_map = {}
        
        queue = deque()
        queue.append((root, 0))
        
        min_dst, max_dst = 0, 0
        
        while queue:
            
            node, dst = queue.popleft()
            
            bottom_view_map[dst] = node.data
            
            min_dst = min(min_dst, dst)
            max_dst = max(max_dst, dst)
            
            if node.left:
                queue.append((node.left, dst-1))
            if node.right:
                queue.append((node.right, dst+1))
                
        result = []
        for i in range(min_dst, max_dst+1):
             result.append(bottom_view_map[i])
        return result
        