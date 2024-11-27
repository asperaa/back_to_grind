class Solution:
    # Handle Case - [1 1 1 1 0 1 1 1 1 1 1] 
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            prev = (mid - 1 + n) % n
            next = (mid + 1) % n
            
            if nums[mid] < nums[prev] and nums[mid] < nums[next]:
                return mid
            elif nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1