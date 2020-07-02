"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1030. Matrix Cells in Distance Order
"""

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            i, j = point
            return abs(r0-i) + abs(c0-j)
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append((i, j))
        return sorted(ans, key=dist)
        