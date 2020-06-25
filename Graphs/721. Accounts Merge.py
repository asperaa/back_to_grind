"""We are the captains of our ship, and we stay 'till the end. We see our stories through.
"""

"""721. Accounts Merge
"""

class Solution:
    
    def accountsMerge(self, accounts):

        email_to_id = {}
        id_to_name = {}
        count = 0
        parent = []
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = count
                    id_to_name[count] = account[0]
                    parent.append(count)
                    count += 1
        rank = [0] * len(parent)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    rank[ry] += 1
        
        for account in accounts:
            for email in account[1:]:
                union(email_to_id[account[1]], email_to_id[email])
        res = {}

        for email, id in email_to_id.items():
            root = find(id)
            res[root] = res.get(root, []) + [email]
        
        return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]

