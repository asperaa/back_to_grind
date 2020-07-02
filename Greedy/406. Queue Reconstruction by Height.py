"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""406. Queue Reconstruction by Height
"""

class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
        
        