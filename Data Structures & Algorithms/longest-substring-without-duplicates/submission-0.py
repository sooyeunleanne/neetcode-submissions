# 3. Longest Substring

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set: # if duplicate appears
                # shrink from the left until valid again
                char_set.remove(s[left])
                left += 1
            # expand right pointer
            char_set.add(s[right])
            #track window size
            max_len = max(max_len, right - left + 1)
        
        return max_len