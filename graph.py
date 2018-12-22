from collections import defaultdict

class Graph(object):
    def __init__(self):
        self._graph = defaultdict(set)

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def size(self):
        return len(self._graph)

    def dfs_topological_sort(self):
        visited = dict.fromkeys(self._graph.keys(), False)
        visited[None] = None
        stack = []

        for i in visited.keys():
            if visited[i] == False:
                self._visit(i, visited, stack)

        print stack

    def _visit(self, i, visited, stack):
        visited[i] = True

        for j in self._graph[i]:
            if visited[j] == False:
                self._visit(j, visited, stack)

        stack.insert(0, i)

