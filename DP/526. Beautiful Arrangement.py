"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""526. Beautiful Arrangement
"""

class Solution:

    def countArrangement(self, n):
        self.ans = 0
        self.total_length = n
        nums = [i for i in range(1, n+1)]
        visited = [False for i in range(n)]
        self.helper(nums, visited, 1)
        return self.ans
    
    def helper(self, nums, visited, count):
        if count == self.total_length + 1:
            self.ans += 1
        else:
            for i in range(self.total_length):
                if not visited[i]:
                    visited[i] = True
                    if nums[i] % count == 0 or count % nums[i] == 0:
                        self.helper(nums, visited, count + 1)
                    visited[i] = False