from graph import Graph

def main():
    graph = Graph()
    graph.add(1, 2)
    graph.add(2, 6)
    graph.add(6, 7)
    graph.add(4, 6)
    graph.add(5, 6)
    graph.add(5, 7)
    graph.add(3, 5)
    graph.add(0, 3)
    graph.add(7, None)

    graph.dfs_topological_sort()

if __name__ == '__main__':
    main()
