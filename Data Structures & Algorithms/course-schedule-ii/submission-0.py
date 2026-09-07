class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses # how many prereqs it still has outstanding


        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []
