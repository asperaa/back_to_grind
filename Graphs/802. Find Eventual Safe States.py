"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""802. Find Eventual Safe States
"""

class Solution:

    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [0] * n

        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = -1
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            visited[i] = 1
            return True
        
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
        not_cyclic = [i for i in range(n) if visited[i]==1]
        return not_cyclic