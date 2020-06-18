"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""131. Palindrome Partitioning
"""

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
            for i in range(0, self.total_length):
                if i + index < self.total_length and self.is_palindrome(s, index, index+i):
                    self.helper(s, curr_set + [s[index:index+i+1]], index+i+1)

    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True
