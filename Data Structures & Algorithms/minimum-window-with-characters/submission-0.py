class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict

        need_hashmap = defaultdict(int)
        # update need_hashmap
        for char in t:
            need_hashmap[char] += 1
        
        need = len(need_hashmap)
        have = 0
        window_hashmap = defaultdict(int)

        response = [-1, -1]
        response_len = float("inf")

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_hashmap[char] += 1

            if char in need_hashmap and need_hashmap[char] == window_hashmap[char]:
                have += 1

            while have == need:
                if (right - left + 1) < response_len:
                    response = [left, right]
                    response_len = right - left + 1

                window_hashmap[s[left]] -= 1
                if s[left] in need_hashmap and window_hashmap[s[left]] < need_hashmap[s[left]]:
                    have -= 1
                
                left += 1
        
        return s[response[0]:response[1]+1] if response_len != float("inf") else ""

