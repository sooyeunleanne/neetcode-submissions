class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n_stairs = len(cost)
        memo = {}

        def dfs(i):
            if i >= n_stairs:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        
        min_cost = min(dfs(0), dfs(1))

        return min_cost