from typing import List
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        par = [-1] * (n+1)
        dist = [float('inf')] * (n+1)
        
        graph = {i: [] for i in range(n+1)}
        
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        pq = []
        
        heapq.heappush(pq, (0, 1, -1))
        
        while pq:
            w, node, p = heapq.heappop(pq)
            dist[node] = w
            par[node] = p
            
            for neighbour, d in graph[node]:
                if dist[neighbour] > w + d:
                    dist[neighbour] = w + d
                    heapq.heappush(pq, (w+d, neighbour, node))
        
        
        if dist[n] == float('inf'):
            return [-1]
        
        ans = []
        p = n
        
        while p != -1:
            ans.append(p)
            p = par[p]
            
        ans.append(dist[n])
        
        ans.reverse()
        
        return ans