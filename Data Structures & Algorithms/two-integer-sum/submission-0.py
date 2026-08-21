class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store seen numbers
        seen = {}
        
        # store seen numbers in number : index format
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i