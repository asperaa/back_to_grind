"""We are the captains of ships, and we stay 'till the end. We see our stories through.
"""

"""785. Is Graph Bipartite?
"""

class Solution:
    
    def isBipartite(self, graph):
        n = len(graph)
        visited = [False] * n
        color = [False] * n
        self.is_same = False
        
        def dfs(i):
            visited[i] = True
            for neighbour in graph[i]:
                if not visited[neighbour]:
                    color[neighbour] = not color[i]
                    dfs(neighbour)
                elif color[i] == color[neighbour]:
                    self.is_same = True
                    break
        

        for i in range(n):
            if not visited[i]:
                dfs(i)
                if self.is_same:
                    return False
        return True

