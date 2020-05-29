"""We are the captains of our ships, and we stay 'till the end. We see our stories through
"""

"""403. Frog Jump [Space and Time - O(n2)]
"""

class Solution:
    
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        cache = {}
        for stone in stones:
            cache[stone] = []
        cache[1] = [1]
        for i in range(1, len(stones)):
            prev_steps = cache[stones[i]]
            for prev_step in prev_steps:
                for step in [prev_step-1, prev_step, prev_step+1]:
                    if step > 0 and step + stones[i] in cache:
                        cache[stones[i]+step].append(step)
        return True if cache[stones[len(stones)-1]] else False

if __name__ == "__main__":
    s = Solution()
    stones = [0,1,3,4,5,7,9,10,12]
    print(s.canCross(stones))

