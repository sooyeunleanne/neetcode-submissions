class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        ptr1, ptr2 = 1, 2
        for _ in range(3, n + 1):
            current = ptr1 + ptr2
            ptr1 = ptr2
            ptr2 = current
        
        return ptr2