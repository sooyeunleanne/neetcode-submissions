class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0

        while left <= right:
            k = (left + right) // 2
            
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + k - 1) // k
            
            if hours_needed <= h: # it works
                res = k
                right = k - 1
            else:
                left = k + 1
            
        return res