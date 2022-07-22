class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited = [False] * numCourses
        recStack = [False] * numCourses

        def isCyclicUntil(node):
            visited[node] = True
            recStack[node] = True

            for neighbor in graph[node]:
                if visited[neighbor] == False:
                    if isCyclicUntil(neighbor) == True:
                        return True
                elif recStack[neighbor] == True:
                    return True
            recStack[node] = False
            return False

        for course in range(numCourses):
            if visited[course] == False:
                if isCyclicUntil(course) == True:
                    return False
        return True


