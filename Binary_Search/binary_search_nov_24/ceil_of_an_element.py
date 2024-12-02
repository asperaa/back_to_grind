
def ceil(nums, target):
    
    left, right = 0, len(nums) - 1
    
    result = -1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    return result