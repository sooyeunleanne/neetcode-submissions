class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temperatures = list(enumerate(temperatures))
        res = [0 for _ in range(len(temperatures))]

        for i, temperature in temperatures:
            if i > 0 and temperatures[i - 1][1] < temperature:
                while stack and stack[-1][1] < temperature:
                    i_item, temp_item = stack.pop()
                    res[i_item] = i - i_item
            
            stack.append((i, temperature))
        
        return res

