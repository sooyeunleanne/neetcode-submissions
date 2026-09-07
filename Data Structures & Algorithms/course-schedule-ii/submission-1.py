class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # creates an adjacency list -- one empty list percourse
        graph = [[] for _ in range(numCourses)]
        # how many prereqs it still has outstanding
        indegree = [0] * numCourses


        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # find every course with zero prerequisites -- these are the courses you can take immediately
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)

            # for every course that depended on node
            for neighbor in graph[node]:
                #decrement its in-degree by 1 (one of its prereqs is now satisfied)
                indegree[neighbor] -= 1

                # all its prereqs are now cleared, so it's ready to be processed
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []
