"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""494. Target Sum [Bottom up]
"""

class Solution:
    
    def findTargetSumWays(self, nums, diff):
        """Find two subsets whose diff is (diff) and whose sum is sum(nums).
           S1 + S2 = sum(nums)
           S1 - S2 = diff (Why? Rearrange the numbers with assigned + and - signs gives this conclusion)
           So, above problem is reduced to subset sum. With S1 = (sum + diff) // 2
        """
        summ = sum(nums)
        s1 = (summ + diff) // 2
        if diff > summ or (summ + diff) % 2 == 1:
            return 0
        self.memo = [[None for _ in range(s1 + 1)] for _ in range(len(nums)+1)]
        return self.num_of_subset_sum(nums, s1)
    
    def num_of_subset_sum(self, nums, s): 
        for i in range(len(nums)+1):
            self.memo[i][0] = 1
        for j in range(1, s+1):
            self.memo[0][j] = 0
        for i in range(1, len(nums)+1):
            for j in range(s+1):
                print("Before", self.memo[len(nums)][s], i, j)
                if j >= nums[i-1]:
                    # print(self.memo[i-1][j], self.memo[i-1][j], self.memo[i-1][j-nums[i-1]] + self.memo[i-1][j])
                    self.memo[i][j] = self.memo[i-1][j-nums[i-1]] + self.memo[i-1][j]
                else:
                    self.memo[i][j] = self.memo[i-1][j]
                print(self.memo[len(nums)][s], i, j)
        print(self.memo)
        return self.memo[len(nums)][s]      

if __name__ == "__main__":
    s = Solution()
    nums = [0,0,0,0,0,0,0,0,1]
    print(s.findTargetSumWays(nums, 1))    