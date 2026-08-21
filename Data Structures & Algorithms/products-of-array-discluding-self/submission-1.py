class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        multiple = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                multiple *= num
        
        output = []
        for num in nums:
            if zero_count > 1:
                output.append(0)
            else:
                if num == 0:
                    output.append(multiple)
                else:
                    if zero_count == 1:
                        output.append(0)
                    else:
                        output.append(int(multiple/num))
        
        return output
