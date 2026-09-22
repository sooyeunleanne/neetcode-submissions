class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n, max_n = 0, 0

        if nums[0] == 1:
            n, max_n = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                max_n = max(n, max_n)
                n = 0
            else:
                n += 1
        
        return max(n, max_n)