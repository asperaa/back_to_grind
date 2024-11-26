class Solution:
    
    def right_binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        right_boundry = -1

        while left <= right:

            mid = left + (right - left) // 2

            if target == nums[mid]:
                right_boundry = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right_boundry
    
    def left_binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        left_boundry = -1
        while left <= right:

            mid = left + (right - left) // 2

            if target == nums[mid]:
                left_boundry = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left_boundry




    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.target_range = []
        l = self.left_binary_search(nums, target)
        r = self.right_binary_search(nums, target)
        return [l, r]
        