"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""813. Largest Sum of Averages [Naive]
"""

class Solution:

    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        summ = [0]*n
        summ[0] = nums[0]
        for i in range(1, n):
            summ[i] = summ[i-1] + nums[i]
        return self.helper(nums, summ, n, 0, k)

    def helper(self, nums, summ, n, s, k):
        if k == 1:
            return (summ[n-1] - summ[s] + nums[s]) / (n - s)
        maxx = float('-inf')
        for i in range(s, n-k+1):
            avg_sum = (summ[i] - summ[s] + nums[s]) / (i-s+1) + self.helper(nums, summ, n, i+1, k-1)
            maxx = max(maxx, avg_sum)
        return maxx

