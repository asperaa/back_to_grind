"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""378. Kth Smallest Element in a Sorted Matrix [Binary Search]
"""
import pdb

class Solution:

    def less_than_equal_count(self, matrix, k, mid, length):
        row, column = length-1, 0
        count = 0
        smaller, larger =  matrix[0][0], matrix[length-1][length-1]
        while row >= 0 and column <= length - 1:
            if matrix[row][column] > mid:
                larger = min(larger, matrix[row][column])
                row -= 1
            else:
                count += row + 1
                smaller = max(smaller, matrix[row][column])
                column += 1
        return count, smaller, larger



    def kthSmallest(self, matrix, k):
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = left + (right - left) // 2
            count, smaller, larger = self.less_than_equal_count(matrix, k, mid, n)
            if count == k:
                return smaller
            elif count < k:
                left = larger
            else:
                right = smaller
        return left


if __name__ == "__main__":
    s = Solution()
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
   ]
    print(s.kthSmallest(matrix, 8))