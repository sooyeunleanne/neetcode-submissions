class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return 0
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            # attach smaller tree under bigger
            parent[rb] = ra
            rank[ra] += rank[rb]
            return 1 # one merge happened
        
        components = n
        for a, b in edges:
            components -= union(a, b)
        
        return components
        
