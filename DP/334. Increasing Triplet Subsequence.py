"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""334. Increasing Triplet Subsequence
"""

class Solution:

    def increasingTriplet(self, nums):
        return self.lis_k(nums, 3)
    
    def lis_k(self, nums, k):
        small_arr = [float('inf')] * (k-1)
        for num in nums:
            for i in range(k-1):
                if num <= small_arr[i]:
                    small_arr[i] = num
                    break
            if num > small_arr[-1]:
                return True
        return False