"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Rod Cutting Bottom Up
"""

def rod_cutting(prices, n):
    if n == 0:
        return 0
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j >= i:
                dp[i][j] = max(prices[i-1]+dp[i][j-i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][n]

if __name__ == "__main__":
    prices = [1, 9, 8] 
    print(rod_cutting(prices, len(prices)))
