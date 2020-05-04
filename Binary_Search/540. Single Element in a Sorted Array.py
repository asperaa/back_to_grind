"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""540. Single Element in a Sorted Array [Walked through fire]
"""

class Solution:

    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if nums[mid] == nums[mid+1]:
                left_half_size = mid - left
                right_half_size = right - mid + 1
                if left_half_size % 2 == 1:
                    right = mid - 1
                else:
                    left = mid
            else:
                left_half_size = mid - left + 1
                right_half_size = right - mid
                if left_half_size % 2 == 1:
                    right = mid
                else:
                    left = mid + 1
        return nums[right]

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3]
    s = Solution()
    print(s.singleNonDuplicate(nums))