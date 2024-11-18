"We are the captains of our ships, we stay 'till the end. We see our stories through."

def coin_change(coins, s):
    n = len(coins)
    dp = [[None for _ in range(s+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = 1
    for j in range(s+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]