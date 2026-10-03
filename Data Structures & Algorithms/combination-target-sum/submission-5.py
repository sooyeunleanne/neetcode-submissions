class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def bt(i, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return
            
            if curr_sum > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            bt(i, curr_sum + nums[i])

            curr.pop()
            bt(i + 1, curr_sum)
        
        bt(0, 0)

        return res



