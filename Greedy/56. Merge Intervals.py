"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""56. Merge Intervals
"""

class Solution:
    
    def merge(self, intervals):
        if not intervals:
            return []
        n = len(intervals)
        intervals.sort()
        low, high = intervals[0][0], intervals[0][1]
        ans = []
        for i in range(1, n):
            if intervals[i][1] > high:
                if intervals[i][0] > high:
                    ans.append([low, high])
                    low = intervals[i][0]
                    high = intervals[i][1]
                else:
                    high = intervals[i][1]
        ans.append([low, high])
        return ans
