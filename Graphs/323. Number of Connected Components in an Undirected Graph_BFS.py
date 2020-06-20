"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""323. Number of Connected Components in an Undirected Graph [BFS]
"""

from collections import deque

class Solution:

    def countComponents(self, n, edges):
        visited = [False for _ in range(n)]
        graph = {i: [] for i in range(n)}
        num_components = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if not visited[i]:
                self.bfs(i, graph, visited)
                num_components += 1
        return num_components
    
    def bfs(self, s, graph, visited):
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
