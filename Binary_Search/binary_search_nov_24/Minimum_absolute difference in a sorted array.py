


def min_diff(nums, key):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if nums[mid] == key:
            return 0
        elif key > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    candidate_1 = abs(nums[left] - key)
    candidate_2 = abs(nums[right] - key)
    return min(candidate_1, candidate_2)