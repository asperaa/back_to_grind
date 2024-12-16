
class Solution:
    
    def partition(self, s):
        n = len(s)
        self.total_length = n
        self.ans = []
        self.helper(s, [], 0)
        return self.ans
    
    def helper(self, s, curr_set, index):
        if index == self.total_length:
            self.ans.append(curr_set)
        else:
            for i in range(self.total_length):
                if i + index < self.total_length and self.is_palin(s, index, index+i):
                    self.helper(s, curr_set + [s[index:index+i]], index+i+1)
    
    def is_palin(s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True