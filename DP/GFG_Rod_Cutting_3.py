"""We are thecaptains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Rod Cut Only 3 ways. [Bottom Up]
"""

def rod_cutting(n, segments):
    dp = [[0 for _ in range(n+1)] for _ in range(3+1)]
    for i in range(1, 3+1):
        for j in range(1, n+1):
            if j > segments[i-1] and dp[i][j-segments[i-1]]:
                dp[i][j] = max(1 + dp[i][j-segments[i-1]], dp[i-1][j])
            elif j == segments[i-1]:
                dp[i][j] = max(1 + dp[i][j-segments[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[3][n]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        segments = [int(i) for i in input().split()]
        print(rod_cutting(n, segments))
        t -= 1