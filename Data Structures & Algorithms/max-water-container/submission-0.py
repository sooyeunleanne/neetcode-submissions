class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        for left in range(len(heights)):
            right = len(heights) - 1

            while left < right:
                area = (right - left) * min(heights[left], heights[right])
                print (left, right)

                if area > max_area:
                    max_area = area
                
                right -= 1
        
        return max_area
