# https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1

from typing import List
from collections import deque


class Solution:
    
    def is_valid(self, i, j, m, n, grid, dist):
        if i>=0 and i<m and j >= 0 and j <n and grid[i][j] == 1 and dist[i][j] == float('inf'):
            return True
        return False
        
    
        
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        queue = deque()
        sr, sc = source
        dr, dc = destination
        
        queue.append((sr, sc))
        dist[sr][sc] = 0
        
        while queue:
            currX, currY = queue.popleft()
            if currX == dr and currY == dc:
                return dist[currX][currY]
            for i in range(4):
                nextX = currX + dx[i]
                nextY = currY + dy[i]
                if self.is_valid (nextX, nextY, m, n, grid, dist):
                    queue.append((nextX, nextY))
                    dist[nextX][nextY] = 1 + dist[currX][currY]
        return -1