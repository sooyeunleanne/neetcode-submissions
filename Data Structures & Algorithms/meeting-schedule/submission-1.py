"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True 
        
        intervals.sort(key = lambda i : i.start)

        prev_s, prev_e = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            s, e = interval.start, interval.end

            if s < prev_e:
                return False
            
            prev_s, prev_e = s, e
        
        return True
