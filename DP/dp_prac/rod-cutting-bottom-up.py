"We are the captains of our ships, we stay 'till the end. We see our stories through."


def rod_cutting(prices):
    n = len(prices)
    length = [i for i in range(n+1)]
        
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if length[i-1] <= j:
                dp[i][j] = max(dp[i][j-length[i-1]], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j])
    return dp[n][n]