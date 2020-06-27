"""We are the captains of ur ships, and we stay 'till the end. We see our stories through.
"""

"""210. Course Schedule II
"""

class Solution:
    
    def findOrder(self, n, edges):
        visited = [False] * n
        rec_stack = [False] * n
        graph = {i: [] for i in range(n)}
        ordering = [-1] * n
        self.curr_pos = n-1
        self.is_cycle = False
        
        def dfs(i):
            visited[i] = True
            rec_stack[i] = True
            for neighbour in graph[i]:
                if not visited[neighbour]:
                    dfs(neighbour)
                elif rec_stack[neighbour] == True:
                    self.is_cycle = True
            ordering[self.curr_pos] = i
            self.curr_pos -= 1
            rec_stack[i] = False

        for u, v in edges:
            graph[v].append(u)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        if self.is_cycle:
            return []
        for node in ordering:
            if node == -1:
                return []
        return ordering