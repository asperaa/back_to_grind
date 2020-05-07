"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""240. Search a 2D Matrix II
"""

class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i >= 0 and i < m and j >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False