class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(o, c, curr):
            if c == n:
                res.append(curr)
                return
            
            if o < n:
                curr += "("
                bt(o + 1, c, curr)
                
                curr = curr[:-1]
            
            if o > c:
                curr += ")"
                bt(o, c + 1, curr)

                curr = curr[:-1]
        
        bt(0, 0, "")

        return res


