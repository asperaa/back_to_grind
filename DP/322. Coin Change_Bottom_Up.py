"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""322. Coin Change
"""

class Solution:
    
    def coinChange(self, coins, amount):
        length = len(coins)
        dp = [[None for _ in range(amount+1)]for _ in range(length+1)]
        for i in range(1, length+1):
            dp[i][0] = 0
        for j in range(0, amount+1):
            dp[0][j] = float('inf') - 1
        for i in range(1, length+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[length][amount] == float('inf') - 1:
            return -1
        else:
            return dp[length][amount]