class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            cur_area = (right - left) * min(heights[left], heights[right])
            max_area = max(cur_area, max_area)

            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        
        return max_area
            
            