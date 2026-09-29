"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 1. Sort by start times
        intervals.sort(key = lambda interval : interval.start)

        # 2. Keep a min-heap of end times
        end_times = []
        
        # 3. For each start time, if the earliest end is <= its start, the room is available, so pop it!
        for interval in intervals:
            if end_times and interval.start >= end_times[0]:
                heapq.heappop(end_times)

            # Push the end time
            heapq.heappush(end_times, interval.end)
        
        return len(end_times)

