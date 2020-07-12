"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1386. Cinema Seat Allocation [Walked through fire - TLE]
"""

class Solution:

    def maxNumberOfFamilies(self, n, seats):
        grid = [[False for _ in range(11)]for _ in range(n+1)]
        for i, j in seats:
            grid[i][j] = True
        total_count = 0
        for i in range(1, n+1):
            row_count = 0
            if not grid[i][2]:
                is_four = 4
                for j in range(2, 6):
                    if not grid[i][j]:
                        is_four -= 1
                if is_four == 0:
                    row_count += 1
            if not grid[i][9]:
                is_four = 4
                for j in range(9, 5, -1):
                    if not grid[i][j]:
                        is_four -= 1
                if is_four == 0:
                    row_count += 1
            if row_count == 0 and not grid[i][4]:
                is_four = 4
                for j in range(4, 8):
                    is_four -= 1
                if is_four == 0:
                    row_count += 1
            total_count += row_count
        return total_count
