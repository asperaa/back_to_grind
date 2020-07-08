"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""135. Candy
"""

class Solution:

    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)

        
         