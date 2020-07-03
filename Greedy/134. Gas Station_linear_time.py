"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""134. Gas Station [T - O(n)]
"""

class Solution:
    
    def canCompleteCircuit(self, gas, cost):
        curr_tank = 0
        n = len(gas)
        ans = 0
        total_gas = 0
        curr_gas = 0
        for i in range(n):
            remaining_gas = gas[i] - cost[i]
            curr_gas += remaining_gas
            total_gas += remaining_gas
            if curr_gas < 0:
                curr_gas = 0
                ans = i + 1
        return ans if total_gas >= 0 else -1
