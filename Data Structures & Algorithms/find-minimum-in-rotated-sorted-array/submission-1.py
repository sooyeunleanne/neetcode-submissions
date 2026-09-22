class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if left == right: 
                break
            
            mid = (left + right) // 2
            
            if nums[mid] <= nums[right]:
                # right half is sorted
                # minimum exists in left half
                right = mid
            else: # nums[mid] > nums[right]
                # minimum exists in right half
                left = mid + 1

        return nums[(left + right) // 2] 