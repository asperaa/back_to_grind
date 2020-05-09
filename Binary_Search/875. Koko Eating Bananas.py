"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""875. Koko Eating Bananas
"""

class Solution:

    def is_valid(self, piles, H, k):
        hours_consumed = 0
        for i in range(len(piles)):
            hours_consumed += piles[i] // k
            hours_consumed += 0 if piles[i] % k == 0 else 1
            if hours_consumed > H:
                return False
        return True


    def minEatingSpeed(self, piles, H):
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            mid = left + (right - left) // 2
            if self.is_valid(piles, H, mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
