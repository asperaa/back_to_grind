"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

def binarySearch_Inceasing(arr, element):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binarySearch_Decreasing(arr, element):
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

def element_finder(arr, element):
    arr_size = len(arr)
    if arr_size == 0:
        return -1
    if arr_size == 1:
        return binarySearch_Inceasing(arr, element)
    if arr[0] < arr[1]:
        return binarySearch_Inceasing(arr, element)
    else:
        return binarySearch_Decreasing(arr, element)


if __name__ == "__main__":
    arr = [5, 4, 3, 2]
    print(element_finder(arr, 2))

