"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""322. Coin Change [Top Down]
"""

class Solution:
    
    def coin_change_helper(self, coins, amount, n, dp):
        if dp[n][amount]:
            return dp[n][amount]
        if n == 0:
            return float('inf') - 1
        if amount == 0:
            return 0
        if amount >= coins[n-1]:
            dp[n][amount] = min(1 + self.coin_change_helper(coins, amount-coins[n-1], n, dp),
                                self.coin_change_helper(coins, amount, n-1, dp))
        else:
            dp[n][amount] = self.coin_change_helper(coins, amount, n-1, dp)
        return dp[n][amount]
    
    def coinChange(self, coins, amount):
        dp = [[None for _ in range(amount+1)]for _ in range(len(coins)+1)]
        ans = self.coin_change_helper(coins, amount, len(coins), dp)
        return ans if ans != float('inf') - 1 else -1