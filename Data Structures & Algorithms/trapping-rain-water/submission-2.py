class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        leftMax = [0 for _ in range(len(height))]
        rightMax = [0 for _ in range(len(height))]

        leftMax_cur, rightMax_cur = 0, 0
        for i in range(len(height)):
            leftMax_cur = max(height[i], leftMax_cur)
            leftMax[i] = leftMax_cur

            rightMax_cur = max(height[len(height) - 1 - i], rightMax_cur)
            rightMax[len(height) - 1 - i] = rightMax_cur
            
        
        for i in range(len(height)):
            water += min(leftMax[i], rightMax[i]) - height[i]
        
        return water
