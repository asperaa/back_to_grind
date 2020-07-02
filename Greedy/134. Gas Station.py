"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""134. Gas Station [T - O(n2)]
"""

class Solution:

    def canCompleteCircuit(self, gas, cost):
        curr_tank = 0
        n = len(gas)
        for i in range(n):
            start = i
            curr_tank = gas[start]
            end = (start + 1) % n
            curr_tank -= cost[start]
            while curr_tank >= 0 and start != end and end < n:
                curr_tank += gas[end]
                curr_tank -= cost[end]
                end += 1
                if end == n:
                    end = 0
            if start == end and curr_tank >= 0:
                return start
        return -1
