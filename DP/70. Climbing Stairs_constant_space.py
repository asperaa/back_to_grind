"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""70. Climbing Stairs [Constant Space]
"""

class Solution:

    def climbStairs(self, n):
        if n <= 2:
            return n 
        first, second = 1, 2
        num_ways = 0
        for _ in range(3, n+1):
            num_ways = first + second
            first = second
            second = num_ways
        return num_ways