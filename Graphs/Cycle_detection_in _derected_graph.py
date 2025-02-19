# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        n = len(adj)
        in_degree = [0]*n
        
        for vertex in range(n):
            for neighbour in adj[vertex]:
                in_degree[neighbour] += 1
                
                
        queue = deque()
        
        for vertex in range(V):
            if in_degree[vertex] == 0:
                queue.append(vertex)
                
        
        processed_count = 0
        
        while queue:
            current_node = queue.popleft()
            processed_count += 1
            
            for neighbour in adj[current_node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return processed_count != n