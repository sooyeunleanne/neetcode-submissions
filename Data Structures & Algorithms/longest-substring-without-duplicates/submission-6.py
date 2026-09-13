class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = {}
        left, right = 0, 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in cur and cur[s[right]] >= left:
                left = cur[s[right]] + 1
                
            cur[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length


