"""We are the captains of our ships, and we stay 'till the end. We see our stories through."""

"""GFG Rod Cutting [Top Down]
"""

def rod_cut_helper(prices, n, curr_length, dp):
    if dp[n][curr_length]:
        return dp[n][curr_length]
    if n == 0 or curr_length == 0:
        return 0
    if curr_length >= n:
        dp[n][curr_length] = max(prices[n-1] + rod_cut_helper(prices, n, curr_length-n, dp),
                                 rod_cut_helper(prices, n-1, curr_length, dp))
    elif curr_length < n:
        dp[n][curr_length] = rod_cut_helper(prices, n-1, curr_length, dp)
    return dp[n][curr_length]

def rod_cut(prices, n):
    dp = [[None for _ in range(n+1)] for _ in range(n+1)]
    return rod_cut_helper(prices, n, n, dp)


if __name__ == "__main__":
    prices = [1, 9, 8] 
    print(rod_cut(prices, len(prices)))