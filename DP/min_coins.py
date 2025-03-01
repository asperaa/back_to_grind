# https://leetcode.com/problems/coin-change/

class Solution:
    

    def min_coins(self, i, s, coins):
        if i==0:
            if s%coins[0] == 0:
                return s // coins[0]
            else:
                return float('inf')
        if self.dp[i][s]:
            return self.dp[i][s]
        not_pick = self.min_coins(i-1, s, coins)
        pick = float('inf')
        if coins[i] < s:
            pick = 1 + self.min_coins(i, s-coins[i], coins)
        self.dp[i][s] = min(pick, not_pick)
        
        return self.dp[i][s]

    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        self.dp = [[None for _ in range(amount+1)] for _ in range(m+1)]
        return self.min_coins(m-1, amount, coins)