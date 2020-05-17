"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
   [Naive recursion]
"""



def subset_sum_helper(arr, s, n):
    if s == 0:
        return True
    if n == 0:
        return False
    if s >= arr[n-1]:
        return subset_sum_helper(arr, s - arr[n-1], n-1) or subset_sum_helper(arr, s, n-1)
    elif s < arr[n-1]:
        return subset_sum_helper(arr, s, n-1)

def is_subset_sum(arr, s):
    length = len(arr)
    return subset_sum_helper(arr, s, length)


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print(is_subset_sum(arr, 9))
