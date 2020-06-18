"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""90. Subsets II
"""

class Solution:

    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        self.total_index = n
        self.ans = []
        self.helper(nums, [], 0)
        return self.ans
    
    def helper(self, nums, curr_set, curr_index):
        self.ans.append(curr_set)
        for i in range(curr_index, self.total_index):
            if i > curr_index and nums[i] == nums[i-1]:
                continue
            self.helper(nums, curr_set + [nums[i]], curr_index + 1)
