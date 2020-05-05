"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1064. Fixed Point
"""

class Solution:

    def fixedPoint(self, A):
        left, right = 0, len(A) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == mid:
                result = mid
                right = mid - 1
            elif A[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return result

