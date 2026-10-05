class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        start, end = newInterval
        res = []

        # before: ends before the new one starts
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        
        # overlapping: starts before new one ends
        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        res.append([start, end])

        # after: starts after new one ends
        while i < n and intervals[i][0] > end:
            res.append(intervals[i])
            i += 1
        
        return res
