"""We are the captains of our ships, we stay 'till the end. We see our stories through.
"""

"""323. Number of Connected Components in an Undirected Graph
"""

class Solution:

    def countComponents(self, n, edges):
        visited = [False for _ in range(n)]
        graph = {i: [] for i in range(n)}
        num_connnected = 0
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        for i in range(n):
            if not visited[i]:
                self.dfs(i, graph, visited)
                num_connnected += 1
        return num_connnected
    
    def dfs(self, i, graph, visited):
        if visited[i]:
            return
        visited[i] = True
        for neighbour in graph[i]:
            self.dfs(neighbour, graph, visited)