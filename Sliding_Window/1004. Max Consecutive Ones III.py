"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1004. Max Consecutive Ones III
"""

class Solution:
    
    def longestOnes(self, num, k):
        start = zeroes = 0
        max_length = 0
        n = len(num)
        for end in range(n):
            if num[end] == 0:
                zeroes += 1
            while zeroes > k:
                if num[start] == 0:
                    zeroes -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length



