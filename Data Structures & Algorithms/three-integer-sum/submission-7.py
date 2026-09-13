class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(enumerate(nums))
        nums.sort(key = lambda x : x[1])
        print(nums)

        res = []

        for first in range(len(nums) - 1):
            if first >= 1 and nums[first][1] == nums[first - 1][1]:
                continue
            
            second = first + 1
            third = len(nums) - 1
            
            while second < third:
                cur = nums[first][1] + nums[second][1] + nums[third][1]
                if cur == 0:
                    res.append([nums[first][1], nums[second][1], nums[third][1]])

                    second += 1
                    while second < third and nums[second][1] == nums[second - 1][1]:
                        second += 1
                    
                    third -= 1
                    while second < third and nums[third][1] == nums[third + 1][1]:
                        third -= 1
                elif cur < 0:
                    second += 1
                    while second < third and nums[second][1] == nums[second - 1][1]:
                        second += 1
                elif cur > 0:
                    third -= 1
                    while second < third and nums[third][1] == nums[third + 1][1]:
                        third -= 1
        
        return res
            