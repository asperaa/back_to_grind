"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1094. Car Pooling
"""

class Solution:

    def carPooling(self, trips, capacity):
        stops = {}
        for people, start, end in trips:
            stops[start] = stops.get(start, 0) + people
            stops[end] = stops.get(end, 0) - people
        for _, people in sorted(stops.items()):
            capacity -= people
            if capacity < 0:
                return False

        return capacity >= 0