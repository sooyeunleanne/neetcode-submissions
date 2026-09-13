class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append(")")
            if char == "{":
                stack.append("}")
            if char == "[":
                stack.append("]")
            
            if char == ")" or char == "}" or char == "]":
                if len(stack) > 0:
                    from_stack = stack.pop()
                else:
                    return False
                
                if char != from_stack:
                    return False
                
        return True if len(stack) == 0 else False