"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""46. Permutations
"""

class Solution:

    def permute(self, nums):
        n = len(nums)
        self.ans = []
        self.total_length = n
        visited = [0] * n
        self.helper(self, nums, 0, [], visited)
        return self.ans
    
    def helper(self, nums, curr_len, curr_permutation, visited):
        if curr_len == self.total_length:
            self.ans.append(curr_permutation)
        else:
            for i in range(self.total_length):
                if visited[i] == 0:
                    visited[i] = 1
                    self.helper(nums, curr_len + 1, curr_permutation + [nums[i]], visited)
                    visited[i] = 0