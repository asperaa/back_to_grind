"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1248. Count Number of Nice Subarrays
"""

class Solution:
    
    def numberOfSubarrays(self, nums, k):
        start = -1
        first_odd_in_win = 0
        ans = 0
        n = len(nums)
        for end in range(n):
            if nums[end] % 2 == 1:
                k -= 1
            if nums[first_odd_in_win] % 2 == 0:
                first_odd_in_win += 1
            if k == 0:
                ans += first_odd_in_win - start
            if k < 0:
                start = first_odd_in_win
                first_odd_in_win += 1
                while nums[first_odd_in_win] % 2 == 0:
                    first_odd_in_win += 1
                k = 0
                ans += first_odd_in_win - start
        return ans
                