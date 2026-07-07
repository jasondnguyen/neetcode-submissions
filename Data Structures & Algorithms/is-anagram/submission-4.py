class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = {}

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for char in t:
            if char in char_freq:
                char_freq[char] -= 1

                if char_freq[char] == 0:
                    del char_freq[char]
            else:
                return False
        
        return char_freq == {}