"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""860. Lemonade Change
"""

class Solution:
    
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten >= 1 and five >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True