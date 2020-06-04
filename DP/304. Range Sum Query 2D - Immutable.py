"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""304. Range Sum Query 2D - Immutable
"""

class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.summ = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.summ[i][j] = matrix[i-1][j-1] + self.summ[i-1][j] + self.summ[i][j-1] - self.summ[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.summ[row2][col2] - self.summ[row2][col1-1] - self.summ[row1-1][col2] + self.summ[row1-1][col1-1]