"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/floor-in-a-sorted-array/
"""

def floor_in_sorted(nums, target, length):
    left, right = 0, length - 1
    result = 0
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    if left == 0 and nums[left] > target:
        return -1
    if left == length:
        return left - 1
    return result
