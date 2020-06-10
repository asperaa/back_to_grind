"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""254. Factor Combinations
"""

class Solution:
    
    def getFactors(self, n):
        factors = self.get_factors(n)
        self.total_length = len(factors)
        if self.total_length == 0:
            return []
        self.ans = []
        self.product = n
        self.helper(factors, [], 1, 0)
        return self.ans
    
    def helper(self, nums, curr_set, curr_pro, curr_index):
        if curr_pro == self.product:
            self.ans.append(curr_set)
        if curr_pro > self.product:
            return
        else:
            for i in range(curr_index, self.total_length):
                self.helper(nums, curr_set + [nums[i]], curr_pro * nums[i], i)

    def get_factors(self, n):
        factor_list = []
        for i in range(2, n//2 + 1):
            if n % i == 0:
                factor_list.append(i)
        return factor_list