from collections import defaultdict

class Graph(object):
    def __init__(self, edges):
        self._graph = defaultdict(set)
        self.add_edges(edges)

    def add_edges(self, edges):
        for node1, node2 in edges:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def size(self):
        len(self._graph)

    def dfs_topological_sort(self):
        visited = [False]*self.size
        stack = []

        for i in range(self.size):
            if visited[i] == False:
                self._visit(i, visited, stack)

        print stack

