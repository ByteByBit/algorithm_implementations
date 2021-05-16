import logging


class Graph:

    def __init__(self, graph: dict):
        
        self.graph = graph
        self.visited = []

    def search(self, start_node: int):

        if start_node not in self.visited: # Is it a stranger node?

            self.visited.append(start_node) # Not anymore.

            for next_node in self.graph[start_node]: # Iterate over it's adjacents.

                self.search(next_node) # Recurse, until we have nodes.


if __name__ == '__main__':

    graph = {0: [1, 2], 1: [3, 4], 2: [6], 3: [5], 4: [], 5: [], 6: []}

    g = Graph(graph=graph)

    g.search(start_node=0) # Fun starts here.

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info(f'Result: {g.visited}')