class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def backtracking(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = nums[i] + max(backtracking(i + 2), backtracking(i + 3))
            return memo[i]   

        return max(backtracking(0), backtracking(1))
