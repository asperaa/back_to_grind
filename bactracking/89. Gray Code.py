"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""89. Gray Code
"""

class Solution:
    
    def grayCode(self, n):
        self.total_length = n
        nums = ["0", "1"]
        if n == 0:
            return [0]
        self.ans = []
        self.helper(nums, "", 0)
        return self.ans
    
    def helper(self, nums, curr_s, count):
        if count  == self.total_length:
            self.ans.append(int(curr_s, 2))
        else:
            for i in range(2):
                if i == 0:
                    self.helper(["0", "1"], curr_s + nums[i], count + 1)
                if i == 1:
                    self.helper(["1", "0"], curr_s + nums[i], count + 1)

