"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""690. Employee Importance
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    
    def getImportance(self, employees, id):
        n = len(employees)
        hash = {employee.id : employee for employee in employees}
        self.ans = 0

        def dfs(id):
            employee = hash[id]
            self.ans += employee.importance
            for subordinate_id in employee.subordinates:
                dfs(subordinate_id)
        
        dfs(id)
        return self.ans