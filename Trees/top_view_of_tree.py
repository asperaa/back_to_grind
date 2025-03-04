# https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

from collections import defaultdict, deque
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
        
        top_view_map = defaultdict(int)
        
        queue = deque()
        queue.append((root, 0))
        
        min_dist = max_dist = 0
        
        while queue:
            
            node, dist = queue.popleft()
            
            if dist not in top_view_map:
                top_view_map[dist] = node.data
            
            if node.left:
                queue.append((node.left, dist-1))
            if node.right:
                queue.append((node.right, dist+1))
                
