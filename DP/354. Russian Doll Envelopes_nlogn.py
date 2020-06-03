"""We are the cpatains of our ships, and we stay 'till the end. We see our stories through.
"""

"""354. Russian Doll Envelopes
"""

class Solution:

    def ceil_in_sorted(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right-left)// 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
    
    def maxEnvelopes(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return n
        nums.sort(key=lambda x:(x[0], -x[1]))
        ans = [nums[0][1]]
        for i in range(1, n):
            if ans[-1] < nums[i][1]:
                ans.append(nums[i][1])
            else:
                pos = self.ceil_in_sorted(ans, nums[i][1])
                ans[pos] = nums[i][1]
        return len(ans)
        