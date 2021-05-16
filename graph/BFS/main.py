import logging
from collections import deque


class Graph:

    def __init__(self, graph: dict, start_node: int):
        
        self.graph = graph
        self.visited = [start_node]
        self.q = deque(self.visited)
        self.start_node = start_node

    def search(self):

        while self.q:

            next_node = self.q.popleft() # Dequeue next vertex.

            for adj_node in self.graph[next_node]: # Iterate over it's adjacent nodes.

                if adj_node not in self.visited: # If it's a competely stranger...

                    self.visited.append(adj_node) # Now it's not.
                    self.q.append(adj_node) # Enqueue it for later fun.


if __name__ == '__main__':

    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    g = Graph(graph=graph, start_node=0)

    g.search() # Fun starts here.

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info(f'Result: {g.visited}')