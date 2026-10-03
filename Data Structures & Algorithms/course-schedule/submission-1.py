class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses # 0 = unvisited, 1 = visiting, 2 = visited
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        def dfs(i):
            if state[i] == 1:
                return False
            if state[i] == 2:
                return True
            
            state[i] = 1
            for course in graph[i]:
                if not dfs(course):
                    return False
            state[i] = 2
            return True
        
        return all(dfs(i) for i in range(numCourses))
                