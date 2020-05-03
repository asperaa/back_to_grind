"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/binary-search/
"""

def binarySearch(arr, element):
    left, right = 0, len(arr)
    while left <= right:
        mid = left + (right - left) // 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    arr = [0, 2, 3]
    print(binarySearch(arr, 3))