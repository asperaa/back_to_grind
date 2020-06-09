"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""78. Subsets
"""

class Solution:
    
    def subsets(self, nums):
        n = len(nums)
        self.total_length = n
        self.arrangement = []
        self.helper([0, 1], [], 0)
        ans = []
        for i in range(len(self.arrangement)):
            subset = []
            for j in range(n):
                if self.arrangement[i][j] == 1:
                    subset.append(nums[j])
            ans.append(subset)
        return ans
    
    def helper(self, nums, curr_set, curr_level):
        if curr_level == self.total_length:
            self.arrangement.append(curr_set)
        else:
            for i in range(len(nums)):
                self.helper(nums, curr_set + [nums[i]], curr_level + 1)