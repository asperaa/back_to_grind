"""We are the captains of our ships, and we stay 'till the end. We see our stories thorugh.
"""

"""1286. Iterator for Combination
"""

class CombinationIterator:
    
    def __init__(self, s: str, k: int):
        n = len(s)
        self.k = k
        self.total_length = n
        self.ans = []
        self.helper(s, "", 0, 0)
        self.iterator = 0
    
    def helper(self, s, curr_s, curr_index, count):
        if count == self.k:
            self.ans.append(curr_s)
        else:
            for i in range(curr_index, self.total_length):
                self.helper(s, curr_s + s[i], i+1, count + 1)

    def next(self) -> str:
        a = self.ans[self.iterator]
        self.iterator += 1
        return a
        

    def hasNext(self) -> bool:
        return self.iterator < len(self.ans)
        
