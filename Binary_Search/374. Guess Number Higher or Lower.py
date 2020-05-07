"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""374. Guess Number Higher or Lower
"""

def guess(num):
    pass

class Solution:


    def guessNumber(self, n):
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result > 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1