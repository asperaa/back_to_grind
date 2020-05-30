"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""656. Coin Path
"""

class Solution:

    def cheapestJump(self, coins, k):
        n = len(coins)
        result = []
        next_arr = [-1 for _ in range(n)]
        self.jump_helper(coins, k, 0, next_arr)
        if next_arr[n-1] == -1:
            return []
        i = 0
        while i < n and next_arr[i] != -1:
            result.append(i+1)
            i = next_arr[i]
        if i == n - 1 and coins[i] >= 0:
            result.append(n)
            return result
        else:
            return []

    
    def jump_helper(self, coins, k, i, next_arr):
        if i == len(coins) - 1 and coins[i] != -1:
            return coins[i]
        min_cost = float('inf')
        for j in range(i+1, i+k+1):
            if coins[i] >= 0 and j < len(coins):
                cost = coins[i] + self.jump_helper(coins, k, j, next_arr)
                if cost < min_cost:
                    min_cost = cost
                    next_arr[i] = j
        return min_cost

