# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        dist = [float('inf')] * V
        
        dist[src] = 0
        
        for _ in range(1, V):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]
                
        return dist