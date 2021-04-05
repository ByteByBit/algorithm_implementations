from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)
        self.visited = set()

    def add_edge(self, u: int, v: int) -> None:

        self.graph[u].append(v)

    
class DFS(Graph):

    '''
    A simple Depth First Search algorithm.
    '''
    
    def __init__(self):

        super().__init__()

    def util(self, v):

        self.visited.add(v)
        print(v)

        for i in self.graph[v]:

            if i not in self.visited:
                self.util(i)

    def search(self, v):

        self.util(v)


if __name__ == '__main__':

    dfs = DFS()
    dfs.add_edge(0, 1)
    dfs.add_edge(0, 2)
    dfs.add_edge(1, 2)
    dfs.add_edge(2, 0)
    dfs.add_edge(2, 3)
    dfs.add_edge(3, 3)

    dfs.search(2)