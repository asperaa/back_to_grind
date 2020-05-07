"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""162. Find Peak Element
"""

class Solution:

    def findPeakElement(self, nums):
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid > 0 and mid < length - 1 and nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif mid == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            elif mid == length - 1:
                if nums[length-1] > nums[length-2]:
                    return length - 1
                else:
                    return length - 2
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else: # nums[mid] < nums[mid-1]
                right = mid - 1
        return left
