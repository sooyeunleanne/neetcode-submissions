class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 2:
                return cost[i]
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i - 2), dp(i - 1))
            return memo[i]
        
        n = len(cost)
        return min(dp(n - 1), dp(n - 2))