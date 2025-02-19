# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

import heapq
 
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        
        n = len(adj)
        dist = [float('inf')] * n
        dist[src] = 0
        pq = []
        heapq.heappush(pq, (0, src))
        
        while pq:
            _, u = heapq.heappop(pq)
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist