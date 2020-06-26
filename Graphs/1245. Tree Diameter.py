"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1245. Tree Diameter
"""

class Solution:

    def treeDiameter(self, edges):
        n = len(edges)
        visited = [False] * (n+1)
        graph = {i: [] for i in range(n+1)}
        self.diameter = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        

        def dfs(i):
            visited[i] = True
            depth_1 = depth_2 = 0
            for child in graph[i]:
                if visited[child]:
                    continue
                depth = dfs(child)
                if depth > depth_1:
                    depth_2 = depth_1
                    depth_1 = depth
                elif depth > depth_2:
                    depth_2 = depth
            self.diameter = max(self.diameter, depth_1 + depth_2)
            return depth_1 + 1
        
        dfs(0)
        return self.diameter
         
