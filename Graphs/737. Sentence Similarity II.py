"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""737. Sentence Similarity II
"""

class Solution:


    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        index = {}
        count = 0
        for pair in pairs:
            if pair[0] not in index:
                index[pair[0]] = count
                count += 1
            if pair[1] not in index:
                index[pair[1]] = count
                count += 1
        parent = list(range(count-1))
        rank = [0] * (count-1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[ry] < rank[ry]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    rank[ry] += 1
        
        for u, v in pairs:
            union(index[u], index[v])
        
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or (w1 in index and w2 in index and find(index[w1]) == find(index[w2])):
                continue
            return False
        return True

