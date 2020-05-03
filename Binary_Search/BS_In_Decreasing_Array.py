"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

def binarySearch(arr, element):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [5, 3, 2]
    print(binarySearch(arr, 5))