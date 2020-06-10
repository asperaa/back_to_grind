"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""17. Letter Combinations of a Phone Number
"""

class Solution:
    
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        self.total_length = n
        self.hash_set = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.ans = []
        self.helper(digits, "", 0, 0)
        return self.ans
    
    def helper(self, digits, curr_set, curr_index, count):
        if count == self.total_length:
            self.ans.append(curr_set)
        else:
            for i in range(curr_index, self.total_length):
                for j in self.hash_set[digits[i]]:
                    self.helper(digits, curr_set + j, i+1, count+1)

