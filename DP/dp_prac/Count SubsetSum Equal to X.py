"We are the captains of our ships, we stay 'till the end. We see our stories through."


def count_subset_sum(arr, s):
    n = len(arr) 
    dp = [[None]*(s+1)]*[n+1]
    
    for i in range(0, n+1):
        dp[i][0] = 1
    
    for j in range(1, s+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[n-1] >= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]
    