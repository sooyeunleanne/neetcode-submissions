class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(houses):
            memo = {}

            def dp(i):
                if i == 1:
                    return max(houses[0], houses[1])
                if i == 0:
                    return houses[0]
                
                if i in memo:
                    return memo[i]
                
                memo[i] = max(houses[i] + dp(i - 2), dp(i - 1))
                return memo[i]
            
            return dp(len(houses) - 1)
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

