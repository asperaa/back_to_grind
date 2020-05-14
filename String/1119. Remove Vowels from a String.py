"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1119. Remove Vowels from a String
"""

class Solution:

    def removeVowels(self, S):
        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        ans = []
        for char in S:
            if char in vowels:
                continue
            ans.append(char)
        return "".join(ans)
