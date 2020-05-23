"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Longest Repeating Subsequence
"""

def longest_repeating_subsequence(s, m):
    dp = [[0 for _ in range(m+1)]for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][m]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m = int(input())
        s = input()
        print(longest_repeating_subsequence(s, m))
        t -= 1