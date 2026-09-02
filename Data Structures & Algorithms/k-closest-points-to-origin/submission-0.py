class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_point_sets = []

        for point in points:
            x, y = point
            distance = pow(x, 2) + pow(y, 2)
            distance_point_set = [distance, x, y]
            distance_point_sets.append(distance_point_set)
        
        heapq.heapify(distance_point_sets)
        result = []
        for _ in range(k):
            item = heapq.heappop(distance_point_sets)
            result.append([item[1], item[2]])
        
        return result