"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""40. Combination Sum II
"""

class Solution:
    
    def combinationSum2(self, nums, target):
        n = len(nums)
        nums.sort()
        self.total_length = n
        self.target = target
        self.ans = []
        visited = [False] * n
        self.helper(nums, 0, [], 0, visited)
        return self.ans
    
    def helper(self, nums, curr_summ, curr_set, index, visited):
        if curr_summ > self.target:
            return
        if curr_summ == self.target:
            self.ans.append(curr_set)
            return
        
        for i in range(index, self.total_length):
            if not visited[i]:
                if i > index and not visited[i-1] and nums[i] == nums[i-1]:
                    continue
                visited[i] = True
                self.helper(nums, curr_summ + nums[i], curr_set + [nums[i]], i+1, visited)
                visited[i] = False