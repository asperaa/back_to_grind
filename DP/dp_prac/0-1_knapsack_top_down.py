"We see our stories through."

def knapsack(weight, values, capacity):
    n = len(weight)
    dp = [[0]*(capacity+1)]*(n+1)
    
    for i in range(1, n+1):
        for j in range(1, capacity + 1):
            if weight[i-1] <= j:
                dp[i][j] = max(values[i] + dp[i-1][j - weight[i-1]], dp[i-1][j])
            elif weight[i-1] > j:
                dp[i[j]] = dp[i-1][j]
    return dp[n][capacity]