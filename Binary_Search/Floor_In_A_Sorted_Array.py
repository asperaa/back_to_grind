"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/floor-in-a-sorted-array/
"""

def floor_in_sorted(nums, target, length):
    left, right = 0, length - 1
    result = -1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
