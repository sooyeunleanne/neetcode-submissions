class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            if char not in freq.keys():
                return False
            freq[char] -= 1
        
        for frequency in freq.values():
            if frequency != 0:
                return False
        
        return True
