class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()

                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()

                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()

                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()

                stack.append(int(float(first) / second))
            else: 
                stack.append(int(token))
        
        return stack.pop()