

def max_subarray_sum(nums, k):
    
    i = j = 0
    n = len(nums)
    
    running_sum = 0
    ans = 0
    
    while j < n:
        
        running_sum += nums[j]
        
        if j-i+1 == k:
            ans = max(ans, running_sum)
            running_sum -= nums[i]
            i += 1
            j += 1            
        else:
            j += 1
    return ans
            
        
        
    