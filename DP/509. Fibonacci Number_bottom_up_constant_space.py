"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""509. Fibonacci Number (Constant space)
"""

class Solution:

    def fib(self, n):
        if n <= 1:
            return n
        if n == 2:
            return 1
        curr = 0
        prev_1 = 1
        prev_2 = 1
        for i in range(3, n+1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return curr