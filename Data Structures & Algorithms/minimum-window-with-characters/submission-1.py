class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        window = {}
        have = 0
        need_count = len(need)
        min_len = float('inf')
        min_left = 0

        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    have += 1
            
            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                left_char = s[left]
                if left_char in need:
                    window[left_char] -= 1
                    if window[left_char] < need[left_char]:
                        have -= 1
                left += 1
            
        if min_len == float('inf'):
            return ""
        
        return s[min_left:min_left+min_len]

        