class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:
            return False
        target = total//2
        memo = {}

        def dp(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums) or remaining < 0:
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = (dp(i + 1, remaining - nums[i]) # take
                                    or dp(i + 1, remaining )) # skip
            return memo[(i, remaining)]
        
        return dp(0, target)