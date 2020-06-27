"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""207. Course Schedule
"""

class Solution:
    
    def canFinish(self, n, edges):
        visited = [False] * n
        rec_stack = [False] * n
        graph = {i: [] for i in range(n)}
        ordering = [-1] * n
        self.curr_pos = n-1

        def dfs(i):
            visited[i] = True
            for neighbour in graph[i]:
                print(neighbour, visited[neighbour])
                if not visited[neighbour]:
                    dfs(neighbour)
                    ordering[self.curr_pos] = i
                    print(ordering)
                    self.curr_pos -= 1
        
        for u, v in edges:
            graph[u].append(v)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        for node in ordering:
            if node == -1:
                return False
        return True
