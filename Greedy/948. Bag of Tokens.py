"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""948. Bag of Tokens
"""

class Solution:
    
    def bagsOfTokensScore(self, tokens, P):
        n = len(tokens)
        left, right = 0, n-1
        points = 0
        while left <= right:
            while P > tokens[left]:
                points += 1
                P -= tokens[left]
                left += 1
            points -= 1
            P += tokens[right]
            right -= 1
        return points

