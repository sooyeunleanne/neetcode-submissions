class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def backtracking(steps):
            if steps == n:
                return 1
            if steps > n:
                return 0
            if steps in memo:
                return memo[steps]
                
            memo[steps] = backtracking(steps + 1) + backtracking(steps + 2)
            return memo[steps]
        
        return backtracking(0)