"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""441. Arranging Coins
"""

class Solution:

    # find the floor of n in the search space of [0, n*(n+1)//2]
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            mid = left + (right-left) // 2
            element_at_mid = (mid * (mid + 1)) // 2
            if element_at_mid == n:
                return mid
            elif element_at_mid < n:
                left = mid + 1
            else:
                right = mid - 1
        return right