"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""209. Minimum Size Subarray Sum
"""

class Solution:
    
    def minSubArrayLen(self, s, num):
        n = len(num)
        min_size = n + 1
        start = 0
        running_sum = 0
        for end in range(n):
            running_sum += num[end]
            while running_sum >= s:
                min_size = min(min_size, end-start + 1)
                running_sum -= num[start]
                start += 1
        if min_size == n+1:
            return 0
        return min_size
