"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""77. Combinations
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        self.ans = []
        self.total_length = n
        self.k = k
        self.helper(nums, [], 0, 0)
        return self.ans
    
    def helper(self, nums, curr_set, index, count):
        if count == self.k:
            self.ans.append(curr_set)
        else:
            for i in range(index, self.total_length):
                self.helper(nums, curr_set + [nums[i]], i+1, count+1)
        