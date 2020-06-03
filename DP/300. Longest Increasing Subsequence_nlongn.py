"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""300. Longest Increasing Subsequence [T - O(nlogn)]
"""

class Solution:

    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        book = [0 for _ in range(n)]
        length = 1
        book[0] = nums[0]
        for i in range(1, n):
            if nums[i] < book[0]:
                book[0] = nums[i]
            elif nums[i] > book[length-1]:
                book[length] = nums[i]
                length += 1
            else:
                ceil_index = self.ceiling_in_sorted(book, 0, length-1, nums[i])
                book[ceil_index] = nums[i]
        return length
    
    def ceiling_in_sorted(self, nums, left, right, target):
        result = -1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result


            