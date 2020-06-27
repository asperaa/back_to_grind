"""886. Possible Bipartition
"""

class Solution:
    
    def possibleBipartition(self, n, edges):
        visited = [False] * (n + 1)
        color = [False] * (n + 1)
        graph = {i: [] for i in range(1, n+1)}
        self.is_same = False

        def dfs(i):
            visited[i] = True
            for neighbour in graph[i]:
                if not visited[neighbour]:
                    color[neighbour] = not color[i]
                    dfs(neighbour)
                elif color[neighbour] == color[i]:
                    self.is_same = True
                    break
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(1, n+1):
            if not visited[i]:
                dfs(i)
                if self.is_same:
                    return False
        return True
            