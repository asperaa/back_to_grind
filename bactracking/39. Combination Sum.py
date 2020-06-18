"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""39. Combination Sum
"""

class Solution:
    
    def combinationSum(self, nums, target):
        n = len(nums)
        self.total_length = n
        self.ans = []
        self.target = target
        self.helper(nums, [], 0, 0)
        return self.ans
    
    def helper(self, nums, curr_set, curr_summ, index):
        if curr_summ == self.target:
            self.ans.append(curr_set)
            return
        elif curr_summ > self.target:
            return
        else:
            for i in range(index, self.total_length):
                self.helper(nums, curr_set + [nums[i]], curr_summ + nums[i], i)
