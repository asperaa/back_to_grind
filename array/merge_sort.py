"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Merge Sort
"""

def merge(arr, l, m, r):
    size_l = m - l + 1
    size_r = r - m
    L = [None] * size_l
    R = [None] * size_r
    for i in range(size_l):
        L[i] = arr[l+i]
    for i in range(size_r):
        R[i] = arr[m+1+i]
    i, j, k = 0, 0, l
    while i < size_l and j < size_r:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < size_l:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < size_r:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + (r-1)) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

if __name__ == "__main__":
    arr = [1, 6, 3, 8, 2]
    print(merge_sort(arr, 0, len(arr)-1))