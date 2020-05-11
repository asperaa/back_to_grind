"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""252. Meeting Rooms
"""

class Solution:

    def canAttendMeetings(self, intervals):
        intervals_by_start_time = sorted(intervals)
        for i in range(len(intervals_by_start_time)-1):
            if intervals_by_start_time[i+1][0] < intervals_by_start_time[i][1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canAttendMeetings([[0, 100], [14, 20], [9, 15]]))