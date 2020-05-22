"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Longest Common Substring
"""

def lc_substring(text1, text2, m, n):
    dp = [[None for _ in range(1+n)]for _ in range(1+m)]
    for i in range(1+m):
        dp[i][0] = 0
    for j in range(1, 1+n):
        dp[0][j] = 0
    ans = 0
    for i in range(1, 1+m):
        for j in range(1, 1+n):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    return ans

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m, n = [int(i) for i in input().split()]
        text1 = input()
        text2 = input()
        print(lc_substring(text1, text2, m, n))
        t -= 1
