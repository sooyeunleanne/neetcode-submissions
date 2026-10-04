class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = curr_min = 1

        for x in nums:
            candidates = (x, x * curr_max, x * curr_min)
            curr_max, curr_min = max(candidates), min(candidates)
            res = max(res, curr_max)
        
        return res