"We are the captains of our ships, we stay 'till the end. We see our stories through."


def peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        
        
        if mid > 1 and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1] and mid < n-1:
            return mid
        elif mid == 0:
            if nums[mid] > nums[mid+1]:
                return mid
        elif mid == len(nums)-1:
            if nums[mid] > nums[mid-1]:
                return mid 
        elif nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid - 1
            
        
    return -1