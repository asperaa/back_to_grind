"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
   [Top Down]
"""

def subset_sum_helper(arr, s, n, dp):
    if s == 0:
        return True
    if n == 0:
        return False
    if dp[n][s]:
        return dp[n][s]
    if s >= arr[n-1]:
        dp[n][s] = subset_sum_helper(arr, s - arr[n-1], n-1, dp) or subset_sum_helper(arr, s, n-1, dp)
        return dp[n][s]
    elif s < arr[n-1]:
        dp[n][s] = subset_sum_helper(arr, s, n-1, dp)
        return dp[n][s]

def isSubsetSum(arr, s):
    length = len(arr)
    dp = [[None] * (s+1)] * (length + 1)
    return subset_sum_helper(arr, s, length, dp)

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print(isSubsetSum(arr, 9))