"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # connected undirected graph
        # should be able to DFS entire graph and create new edges/nodes as we go
        # type of graph representation: adjacency list

        # clone_graph = [[] for i in range(len(node))]

        old_new = {}

        def dfs(node):
            if node in old_new:
                return old_new[node]
            copy = Node(node.val)
            old_new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None







