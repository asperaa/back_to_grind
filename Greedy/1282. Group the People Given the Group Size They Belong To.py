"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1282. Group the People Given the Group Size They Belong To
"""

class Solution:

    def groupThePeople(self, groupSizes):
        n = len(groupSizes)
        group_id_to_people = {}
        for i in range(n):
            if groupSizes[i] in group_id_to_people:
                group_id_to_people[groupSizes[i]].append(i)
            else:
                group_id_to_people[groupSizes[i]] = [i]
        ans = []
        for key, values in group_id_to_people.items():
            for i in range(len(values)):
                sub_ans = []
                for j in range(i, i+key):
                    sub_ans.append(values[j])
                ans.append(sub_ans)
        return ans
