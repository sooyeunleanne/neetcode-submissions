class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            memo[i] = False
            for w in wordDict:
                if s.startswith(w, i) and dp(i + len(w)):
                    memo[i] = True
                    break
            
            return memo[i]
        
        return dp(0)
