"""We are the captains of our ships, and we stay 'till the end. We see our stories through."""

"""474. Ones and Zeroes [Naive]
"""

class Solution:
    
    def findMaxFormHelper(self, zeroes_and_ones, zeroes, ones, n):
        if n == 0:
            return 0
        if zeroes >= zeroes_and_ones[n-1][0] and ones >= zeroes_and_ones[n-1][1]:
            return max(1 + self.findMaxFormHelper(zeroes_and_ones, zeroes - zeroes_and_ones[n-1][0], ones - zeroes_and_ones[n-1][1], n-1),
                       self.findMaxFormHelper(zeroes_and_ones, zeroes, ones, n-1))
        else:
             return self.findMaxFormHelper(zeroes_and_ones, zeroes, ones, n-1)
    
    def findMaxForm(self, strs, m, n):
        zeroes_and_ones = []
        for s in strs:
            zero_count = one_count = 0
            for c in s:
                if c is "0":
                    zero_count += 1
                else:
                    one_count += 1
            zeroes_and_ones.append((zero_count, one_count))
        return self.findMaxFormHelper(zeroes_and_ones, m, n, len(strs))