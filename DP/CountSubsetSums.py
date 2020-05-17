"""We are the captains of ur ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/
"""

def subset_sum_helper(arr, s, n, dp):
    if s == 0:
        return 1
    if n == 0:
        return 0
    if dp[n][s]:
        return dp[n][s]
    if s >= arr[n-1]:
        dp[n][s] = subset_sum_helper(arr, s-arr[n-1], n-1, dp) + subset_sum_helper(arr, s, n-1, dp)
    elif s < arr[n-1]:
        dp[n][s] = subset_sum_helper(arr, s, n-1, dp)
    return dp[n][s]

def count_subset_sum(arr, s):
    length = len(arr)
    dp = [[None for _ in range(s+1)] for _ in range(length+1)]
    return subset_sum_helper(arr, s, length, dp)

if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    print(count_subset_sum(arr, 10))