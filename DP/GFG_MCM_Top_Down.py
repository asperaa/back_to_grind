"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""MCM Top Down
"""

def mcm_helper(num, i, j, dp):
    if i >= j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    min_cost = float('inf')
    for k in range(i, j):
        if dp[i][k]:
            left_cost = dp[i][k]
        else:
            left_cost = mcm_helper(num, i, k, dp)
        if dp[k+1][j]:
            right_cost = dp[k+1][j]
        else:
            right_cost = mcm_helper(num, k+1, j, dp)
        curr_cost = num[i-1] * num[k] * num[j]
        total_curr_cost = left_cost + right_cost + curr_cost
        min_cost = min(min_cost, total_curr_cost)
    dp[i][j] = min_cost
    return min_cost

def mcm(nums, m):
    dp = [[None for _ in range(m+1)]for _ in range(m+1)]
    return mcm_helper(nums, 1, m-1, dp)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m = int(input())
        arr = [int(i) for i in input().split()]
        print(mcm(arr, m))
        t -= 1