class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        from collections import defaultdict
        graph = defaultdict(list)
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def DFS(source):
            visited[source] = True
            for neighbor in graph[source]:
                if visited[neighbor] == False:
                    DFS(neighbor)

        count = 0
        for node in range(n):
            if visited[node] == False:
                count += 1
                DFS(node)

        return count

