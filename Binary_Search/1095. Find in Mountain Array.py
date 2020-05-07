"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1095. Find in Mountain Array
"""

class Solution:

    def findInMountainArray(self, target, mountain_arr):
        length = mountain_arr.length()
        left, right = 0, length - 1
        max_element_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = mountain_arr.get(mid)
            if mid_element > mountain_arr.get(mid+1) and mid_element > mountain_arr.get(mid-1):
                max_element_index = mid
                break
            elif mid_element < mountain_arr.get(mid+1):
                left = mid + 1
            else:
                right = mid - 1
        target_in_left = self.binary_search_increasing(mountain_arr, 0, max_element_index, target)
        if target_in_left == -1:
            return self.binary_search_decreasing(mountain_arr, max_element_index+1, length-1, target)
        return target_in_left
    
    def binary_search_increasing(self, mountain_arr, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = mountain_arr.get(mid)
            if mid_element == target:
                return mid
            elif mid_element > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def binary_search_decreasing(self, mountain_arr, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = mountain_arr.get(mid)
            if mid_element == target:
                return mid
            elif mid_element > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
