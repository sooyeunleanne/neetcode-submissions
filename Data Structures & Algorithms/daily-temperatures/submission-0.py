class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev = stack.pop()
                answer[prev] = i - prev
            
            stack.append(i)
        
        return answer

            
