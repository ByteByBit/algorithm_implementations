class Graph:

    def __init__(self, v: int, s: int) -> None:
        
        self.num_vertices = v
        self.g = []
        self.source = s

    def add_edge(self, m: int, n: int, w: int):

        self.g.append([m, n, w])

    def BellmanFord(self):

        inf = float('Inf')

        distances = [inf] * self.num_vertices # Init all distances as infinite.

        distances[self.source] = 0 # Set source distance to null.

        for _ in range(self.num_vertices - 1): # relax edges |V| - 1 times.

            for m, n, w in self.g: # Iterate over each edge, vertex and weight.

                if distances[m] != inf and distances[m] + w < distances[n]:
                    
                    distances[n] = distances[m] + w

        # Final loop to validate that no negative cycles exist in the graph.
        for m, n, w in self.g:

            if distances[m] != inf and distances[m] + w < distances[n]:
                print('Negative cycle...')
                return None


        return distances


if __name__ == '__main__':

    g = Graph(5, 0)

    g.add_edge(0, 1, -1) 
    g.add_edge(0, 2, 4) 
    g.add_edge(1, 2, 3) 
    g.add_edge(1, 3, 2) 
    g.add_edge(1, 4, 2) 
    g.add_edge(3, 2, 5) 
    g.add_edge(3, 1, 1) 
    g.add_edge(4, 3, -3)

    res = g.BellmanFord()
    print(res)