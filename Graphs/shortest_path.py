# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1


from collections import deque

class Solution:
    def shortestPath(self, adj, src):
        
        n = len(adj)
        dist = [float('inf')] * n
        
        
        queue = deque()
        queue.append(src)
        dist[src] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbour in adj[node]:
                if dist[node] + 1 < dist[neighbour]:
                    dist[neighbour] = dist[node] + 1
                    queue.append(neighbour)
        
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
                
                
        return dist