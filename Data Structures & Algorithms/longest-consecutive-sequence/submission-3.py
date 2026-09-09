class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        consec = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] - nums[i-1] == 1:
                consec += 1
            else:
                longest = max(consec, longest)
                consec = 1
        
        return max(consec, longest)