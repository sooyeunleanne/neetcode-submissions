class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in mapping:  # opening bracket
                stack.append(mapping[char])  # push expected closing
            else:  # closing bracket
                if not stack or stack.pop() != char:
                    return False
        
        return not stack  # True if stack is empty