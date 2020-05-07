"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""240. Search a 2D Matrix II
"""

class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            pivot_index = left + (right-left) // 2
            pivot_element = matrix[pivot_index//n][pivot_index%n]
            if pivot_element == target:
                return True
            elif pivot_element > target:
                right = pivot_index - 1
            else:
                left = pivot_index + 1


        return False