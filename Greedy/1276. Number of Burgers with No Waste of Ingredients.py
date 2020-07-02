"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1276. Number of Burgers with No Waste of Ingredients
"""

class Solution:

    def numOfBurgers(self, T: int, C: int):
        ans = []
        if (T - 2 * C) % 2 == 0 and (T-2*C)//2 >= 0:
            ans.append((T-2*C)//2)
        else:
            return []
        if (4 * C - T) % 2 == 0 and (4*C-T)//2 >= 0:
            ans.append((4*C-T)//2)
        else:
            return []
        return ans
    
            
        