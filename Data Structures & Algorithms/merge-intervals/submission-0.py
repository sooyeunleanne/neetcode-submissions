class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p_start, p_end = intervals[0]

        res = []
        for start, end in intervals[1:]:
            if start <= p_end:
                p_end = max(end, p_end)
            else:
                res.append([p_start, p_end])
                p_start, p_end = start, end
        
        res.append([p_start, p_end])
        return res

            
            
