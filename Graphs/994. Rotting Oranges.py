"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""994. Rotting Oranges
"""

from collections import deque

class Solution:

    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maxx = 0
        fresh = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            x, y, d = queue.popleft()
            maxx = max(maxx, d)
            for dirr in directions:
                new_x, new_y = x + dirr[0], y + dirr[1]
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y, d+1))
                    fresh -= 1
        return maxx if fresh == 0 else -1