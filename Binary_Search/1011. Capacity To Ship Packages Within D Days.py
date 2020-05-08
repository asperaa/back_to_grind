"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1011. Capacity To Ship Packages Within D Days
"""

class Solution:

    def shipWithinDays(self, weights, D):
        left = max(weights)
        right = sum(weights)
        capacity = right
        while left <= right:
            potential_capacity = left + (right-left) // 2
            if self.is_valid(weights, D, potential_capacity):
                capacity = potential_capacity
                right = potential_capacity - 1
            else:
                left = potential_capacity + 1
        return capacity
    
    def is_valid(self, weights, D, capacity):
        num_of_days = 1
        load_of_day = 0
        for i in range(len(weights)):
            load_of_day += weights[i]
            if load_of_day > capacity:
                load_of_day = weights[i]
                num_of_days += 1
            if num_of_days > D:
                return False
        return True