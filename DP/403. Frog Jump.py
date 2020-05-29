"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""403. Frog Jump [Walked through fire]
"""

class Solution:
    
    def canCross(self, stones):
        self.cache = {}
        self.valid_stones = {}
        for stone in stones:
            self.valid_stones[stone] = True
        self.last_index = len(stones) - 1
        ans = self.helper(stones, 1, 1, 1) 
        return ans
    
    def helper(self, stones, curr_pos, prev_jump, curr_index):
        key = "#".join([str(curr_pos), str(curr_index), str(prev_jump)])
        if prev_jump <= 0:
            return False
        if key in self.cache:
            return self.cache[key]
        if curr_pos == stones[self.last_index]:
            return True
        if curr_pos in self.valid_stones:
            first_try = self.helper(stones, curr_pos+prev_jump-1, prev_jump-1, curr_index+1)
            second_try = self.helper(stones, curr_pos+prev_jump, prev_jump, curr_index+1)
            third_try = self.helper(stones, curr_pos+prev_jump+1, prev_jump+1, curr_index+1)
            self.cache[key] = can_cross = first_try or second_try or third_try
        else:
            self.cache[key] = can_cross = False
        
        # can_cross = first_try or second_try or third_try

        return can_cross