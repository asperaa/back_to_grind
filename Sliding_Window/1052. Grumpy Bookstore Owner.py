"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1052. Grumpy Bookstore Owner
"""

class Solution:
    
    def maxSatisfied(self, customers, grumpy, k):
        curr_sum = curr_sum_grump = 0
        start = end = 0
        n = len(customers)
        max_diff = 0
        ans = 0
        for i in range(n):
            curr_sum += customers[i]
            curr_sum_grump += customers[i] * (grumpy[i] == 0)
            if i >= k - 1:
                diff = curr_sum - curr_sum_grump
                if max_diff < diff:
                    max_diff = diff
                    start = i - k + 1
                    end = i
                curr_sum -= customers[i-k+1]
                curr_sum_grump -= customers[i-k+1] * (grumpy[i-k+1] == 0)
        for i in range(start, end+1):
            grumpy[i] = 0
        for i in range(n):
            ans += customers[i] * (grumpy[i] == 0)
        return ans


