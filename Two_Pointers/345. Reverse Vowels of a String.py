"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""345. Reverse Vowels of a String
"""

class Solution:
    
    def reverseVowels(self, s):
        str_list = list(s)
        start, end = 0, len(str_list) - 1
        vowels = {
                  'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
                  'A': True, 'E': True, 'I': True, 'O': True, 'U': True
                 }
        while start <= end:
            if str_list[start] in vowels and str_list[end] in vowels:
                temp = str_list[end]
                str_list[end] = str_list[start]
                str_list[start] = temp
                start += 1
                end -= 1
                continue
            if not str_list[start] in vowels:
                start += 1
            if not str_list[end] in vowels:
                end -= 1
        return "".join(str_list)       