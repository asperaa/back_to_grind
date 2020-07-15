"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/
"""

def MaxSubSum(arr, k):
    max_so_far = float('-inf')
    n = len(arr)
    running_sum = 0
    for i in range(n):
        running_sum += arr[i]
        if i >= k - 1:
            max_so_far = max(max_so_far, running_sum)
            running_sum -= arr[i - k + 1]
    return max_so_far

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        print(MaxSubSum(arr, k))
        t -= 1
