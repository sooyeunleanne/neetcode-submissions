class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[1])
        
        removed = 0
        prev_s, prev_e = intervals[0]
        for s, e in intervals[1:]:
            if s >= prev_e:
                prev_e = e # keep it
            else:
                removed += 1 # overlaps, drop it
        
        return removed