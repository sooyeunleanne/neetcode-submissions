class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] #store indices of increasing bar heights
        max_area = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    #the tallest index as of now - the most recent stack item index
                    w = i - stack[-1] - 1 #why
                else:
                    w = i

                area = h * w

                if area > max_area:
                    max_area = area
            
            stack.append(i)
        
        return max_area
