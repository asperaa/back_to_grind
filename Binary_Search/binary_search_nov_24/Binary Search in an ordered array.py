"We are the captains of our ships, and we stay 'till the end. We see our stories through."


def binary_search_increasing_order(arr, element):
    left, right = 0, ;len(arr) - 1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if element > arr[mid]:
            left = mid + 1
        elif element < arr[mid]:
            right = mid - 1
        elif element == arr[mid]:
            return mid
    return -1


def binary_search_decreasing_order(arr, element):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if element == arr[mid]:
            return mid
        elif element > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1