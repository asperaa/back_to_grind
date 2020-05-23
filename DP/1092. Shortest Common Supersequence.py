"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""GFG. Shortest Common Supersequence Length [Bottom Up]
"""

def shortestCommonSupersequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[None for _ in range(n+1)]for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return m + n - dp[m][n]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        text1, text2 = [i for i in input().split()]
        print(shortestCommonSupersequence(text1, text2))
        t -= 1