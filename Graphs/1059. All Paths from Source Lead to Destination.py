"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1059. All Paths from Source Lead to Destination
"""

class Solution:

    def leadsToDestination(self, n, edges, s, d):
        visited = [0] * n
        graph = [[] for _ in range(n)]

        def dfs(i):
            if len(graph[i]) == 0:
                return i == d
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

        for u, v in edges:
            graph[u].append(v)
        dfs(s)