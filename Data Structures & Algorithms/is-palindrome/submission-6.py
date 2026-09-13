class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        processed = ""
        for char in s:
            if char.isalnum():
                processed += char


        left = 0
        right = len(processed) - 1

        while left < right:
            if processed[left] != processed[right]:
                return False
            
            left += 1
            right -= 1
        

        return True