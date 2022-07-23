class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        visited, cycle = set(), set()
        res = []

        def DFS(source):
            if source in visited:
                return True
            if source in cycle:
                return False

            cycle.add(source)

            for neighbor in graph[source]:
                if neighbor not in visited:
                    if DFS(neighbor) == False:
                        return False

            cycle.remove(source)
            res.append(source)
            visited.add(source)

        for course in range(numCourses):
            if course not in visited:
                if DFS(course) == False:
                    return []

        return res




