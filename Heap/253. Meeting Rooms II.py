"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""253. Meeting Rooms II
"""

from heapq import heappop, heappush

class Solution:

    def minMeetingRooms(self, intervals):
        min_heap = []
        intervals = sorted(intervals)
        for start_time, end_time in intervals:
            if min_heap and min_heap[0] <= start_time:
                heappop(min_heap)
            heappush(min_heap, end_time)
        return len(min_heap)       
