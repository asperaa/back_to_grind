

def is_subset_sum_helper(n, arr, s):
    if s == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] <= s:
        return is_subset_sum_helper(n-1, arr, s-arr[n-1]) or is_subset_sum_helper(n-1, arr, s)
    if arr[n-1] > s:
        return is_subset_sum_helper(n-1, arr, s)


def is_subset_sum(arr, s):
    n = len(arr)
    return is_subset_sum_helper(n, arr, s)
