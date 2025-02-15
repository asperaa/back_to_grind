# https://www.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self, i, adj, visited, stack):
        visited[i] = True
        
        for neighbour in adj[i]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj, visited, stack)
        
        stack.insert(0, i)
    
    
    
    def topologicalSort(self,adj):
        
        n = len(adj)
        visited = [False] *  n
        stack = []
        
        for i in range(n):
            if not visited[i]:
                self.dfs(i, adj, visited, stack)
                
        return stack