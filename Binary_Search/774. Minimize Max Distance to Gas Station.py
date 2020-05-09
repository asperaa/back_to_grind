"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""774. Minimize Max Distance to Gas Station
"""
from math import ceil

class Solution:

    def is_valid(self, stations, K, distance):
        num_gas_stations = 0
        for i in range(len(stations) - 1):
            num_gas_stations += ceil((stations[i+1]-stations[i]) / distance) - 1
            if num_gas_stations > K:
                return False
        return True

    def minmaxGasDist(self, stations, K):
        left, right = 0, stations[-1] - stations[0]
        min_distance = right
        while left < right - 1e-6:
            mid = (left + right) / 2
            if self.is_valid(stations, K, mid):
                min_distance = mid
                right = mid
            else:
                left = mid
        return min_distance

