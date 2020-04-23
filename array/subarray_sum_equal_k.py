"""We are the captains of our ships, and we stay 'till the end. We see our stories through."""

"""560. Subarray Sum Equals K
"""

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = []
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix_sum.append(summ)
        sum_hash = {0:1}
        for summ in prefix_sum:
            if summ - k in sum_hash:
                count += sum_hash[summ-k]
            if summ in sum_hash:
                sum_hash[summ] += 1
            else:            
                sum_hash[summ] = 1
        return count  

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1], 0))