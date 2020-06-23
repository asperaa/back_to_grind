"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1162. As Far from Land as Possible
"""

from collections import deque

class Solution:

    def maxDistance(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        maxx = -1
        visited = [[False for _ in range(n)]for _ in range(m)]
        queue = deque()
        summ = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    queue.append((i, j, 0))
                    summ += 1
        while queue:
            x, y, d = queue.popleft()
            maxx = max(maxx, d)
            for dirr in directions:
                new_x, new_y = x + dirr[0], y + dirr[1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, d+1))
        # no water case
        if summ == m * n:
            return -1
        return maxx
