# 567. Permutation in String

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)

        # load all the frequencies of s1
        for s1_char in s1:
            s1_freq[s1_char] += 1

        left = 0
        for right in range(len(s2)):
            # add right char
            s2_freq[s2[right]] += 1

            window_size = right - left + 1
            # if window size bigger than s1
            if window_size > len(s1):
                # slide, remove the left char
                s2_freq[s2[left]] -= 1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]
                left += 1
            
            if s1_freq == s2_freq:
                return True
        
        return False