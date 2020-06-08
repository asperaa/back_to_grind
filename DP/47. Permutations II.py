"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""47. Permutations II
"""

class Solution:
    
    def permuteUnique(self, nums):
        n = len(nums)
        self.total_length = n
        if not nums:
            return []
        self.ans = []
        visited = [False] * n 
        nums.sort()
        self.helper(nums, 0, [], visited)
        return self.ans
    
    def helper(self, nums, curr_len, curr_permute, visited):
        if curr_len == self.total_length:
            self.ans.append(curr_permute)
        else:
            for i in range(self.total_length):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:
                        continue
                    visited[i] = True
                    self.helper(nums, curr_len + 1, curr_permute + [nums[i]], visited)
                    visited[i] = False