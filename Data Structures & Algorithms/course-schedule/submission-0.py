class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # treat courses as nodes and prereq as directed edges
        # you can finish all courses iff the graph has no cycle
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(node):
            if state[node] == 1:
                return False #cycle found
            if state[node] == 2:
                return True # confirmed safe
            
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        
        return all(dfs(i) for i in range(numCourses))