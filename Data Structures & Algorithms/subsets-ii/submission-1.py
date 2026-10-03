class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j + 1)

                curr.pop()
                dfs(j + 1)
        
        dfs(0)

        return res
