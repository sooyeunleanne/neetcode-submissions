class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combi = []

        def backtracking(i, curr):
            if curr == target:
                res.append(combi.copy())
                return
            
            if curr > target or i >= len(nums):
                return
            
            combi.append(nums[i])
            backtracking(i, curr + nums[i])

            combi.pop()
            backtracking(i + 1, curr)
        
        backtracking(0, 0)

        return res
            
