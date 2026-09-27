class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_set = []

        def backtracking(i, curr_sum):
            if curr_sum > target or i >= len(nums):
                return
            
            if curr_sum == target:
                res.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            backtracking(i, curr_sum + nums[i])
            
            curr_set.pop()
            backtracking(i + 1, curr_sum)
        
        backtracking(0, 0)

        return res


