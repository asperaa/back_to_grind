"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""320. Generalized Abbreviation
"""

class Solution:

    def generateAbbreviations(self, word):
        n = len(word)
        self.total_length = n
        self.ans = []
        self.helper(word, "", 0, 0)
        return self.ans
    
    def helper(self, word, curr_word, curr_index, count):
        if curr_index == self.total_length:
            self.ans.append(curr_word + str(count) if count > 0 else curr_word)
        else:
            self.helper(word, curr_word, curr_index + 1, count + 1) # Dont abreviate
            self.helper(word, curr_word + (str(count) if count > 0 else "") + word[curr_index], curr_index + 1, 0)
            
