class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 0
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # breakpoint is in the right side
                left = mid + 1
            else:
                right = mid
        
        return nums[(left + right) // 2]
                

            