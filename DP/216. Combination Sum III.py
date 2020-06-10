"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""216. Combination Sum III
"""

class Solution:
    

    def combinationSum3(self, k, n):
        nums = [i for i in range(1, 10)]
        self.ans = []
        self.k = k
        self.summ = n
        self.helper(nums, [], 0, 0, 0)
        return self.ans
    
    def helper(self, nums, curr_set, curr_sum, count, curr_index):
        if curr_sum > self.summ or count > self.k:
            return
        if curr_sum == self.summ and count == self.k:
            self.ans.append(curr_set)
            return
        else:
            for i in range(curr_index, len(nums)):
                self.helper(nums, curr_set + [nums[i]], curr_sum + nums[i], count + 1, i+1)
