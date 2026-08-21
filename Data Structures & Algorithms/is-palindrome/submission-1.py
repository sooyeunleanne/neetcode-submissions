class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        s_length = len(s)
        for s_index in range(len(s) // 2):
            opp_s_index = s_length - s_index - 1

            if s[s_index] != s[opp_s_index]:
                return False

        return True