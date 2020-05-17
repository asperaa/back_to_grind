"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
   [Bottom Up]
"""

def IsSubsetSum(arr, s):
    num_of_elements = len(arr)
    dp = [[None for i in range(s+1)]  
            for i in range(num_of_elements+1)]
    for i in range(num_of_elements + 1):
        dp[i][0] = True
    for j in range(1, s+1):
        dp[0][j] = False
    for i in range(1, num_of_elements + 1):
        for j in range(1, s + 1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
            elif j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
    return dp[num_of_elements][s]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print(IsSubsetSum(arr, 30))