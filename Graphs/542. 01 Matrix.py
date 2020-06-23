"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""542. 01 Matrix
"""

from collections import deque

class Solution:

    def updateMatrix(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(n)]for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for dirr in directions:
                new_x, new_y = x + dirr[0], y + dirr[1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                    grid[new_x][new_y] = grid[x][y] + 1
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
        return grid            
            