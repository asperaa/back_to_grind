"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
"""

def ceiling_in_sorted(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
