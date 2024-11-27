


def floor(nums, target):
    left, right = 0, len(nums)
    result = -1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            result = mid     # storing this element because it is possible candidate
            left = mid + 1
        else:
            right = mid - 1
    return result