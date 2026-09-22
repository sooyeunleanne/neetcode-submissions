class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums_forward = [1, 1, 2, 8]
        # nums_backward = [48. 24, 6, 1]

        n = len(nums)
        nums_forward = [1] * n
        nums_backward = [1] * n

        for i in range(1, n):
            nums_forward[i] = nums[i - 1] * nums_forward[i - 1]
        
        for i in range(n - 2, -1, -1):
            nums_backward[i] = nums[i + 1] * nums_backward[i + 1]
        
        res = [1] * n
        for i in range(n):
            res[i] = nums_forward[i] * nums_backward[i]

        return res