# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1


from typing import List


class Solution:
    
    
    def findTopoSort(self, node, adj, vis, stack):
        vis[node] = True
        for neighbour, weight in adj[node]:
            if not vis[neighbour]:
                self.findTopoSort(neighbour, adj, vis, stack)
        stack.append(node)
    
    
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(V)}
        
        for u, v, weight in edges:
            graph[u].append((v, weight))
        
        visited = [False] * V
    
        src = 0
        dist = [10**9] * V
        dist[src] = 0
        stack = []
        
        for i in range(V):
            if not visited[i]:
                self.findTopoSort(i, graph, visited, stack)
        
        while stack:
            
            node = stack.pop()
            
            if dist[node] != 10**9:
                for neighbour, weight in graph[node]:
                    if dist[node] + weight < dist[neighbour]:
                        dist[neighbour] = dist[node] + weight
        
        
        for i in range(V):
            if dist[i] == 10**9:
                dist[i] = -1
        return dist