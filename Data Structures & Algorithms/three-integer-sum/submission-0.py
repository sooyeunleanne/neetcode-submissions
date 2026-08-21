class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        solution_set = []
        for first in range(len(nums) - 2):
            # skip duplicates 
            if first > 0 and nums[first] == nums[first - 1]:
                continue
                
            second = first + 1
            third = len(nums) - 1
            
            while second < third:
                sum_total = nums[first] + nums[second] + nums[third]

                if sum_total < 0:
                    second += 1
                elif sum_total > 0:
                    third -= 1
                else:
                    solution_set.append([nums[first], nums[second], nums[third]])

                    # skip duplicates 
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    
                    second += 1
                    third -= 1

        return solution_set
