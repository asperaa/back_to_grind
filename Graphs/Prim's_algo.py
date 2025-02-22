# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        min_heap = []
        
        visited = [False] * V
        
        heapq.heappush(min_heap, (0, 0))
        
        total_weight = 0
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            visited[u] = True
            total_weight += weight
            
            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
        return total_weight