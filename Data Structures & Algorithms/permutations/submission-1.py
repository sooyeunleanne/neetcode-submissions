class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []

        def bt():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    bt()
                    curr.pop()

        bt()

        return res