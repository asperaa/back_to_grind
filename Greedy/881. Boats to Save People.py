"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""881. Boats to Save People
"""

class Solution:
    
    def numRescueBoats(self, people, limit):
        people.sort()
        n = len(people)
        start, end = 0, n - 1
        count = 0
        while start <= end:
            if people[end] + people[start] <= limit:
                start += 1
            end -= 1
            count += 1
        return count