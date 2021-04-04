
class Edge:
    '''
    A class used to represent an edge of a network.
    '''

    def __init__(
        self, start:str = '', end:str = '', capacity:int = 0, 
        source:bool = False, sink:bool = False):
        '''       
        Parameters
        ----------
        start : str 
            Start node of the edge.
        end : str
            End node of the edge.
        capacity : int, optional
            Capacity of the node (default is 0).
        '''

        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.return_edge = None
        self.source = source
        self.sink = sink


class Vertex:
    '''
    A class used to represent a vertex of a network.
    '''

    def __init__(
        self, name:str = '', source:bool = False, sink:bool = False):
        '''
        Parameters
        ----------
        name : str 
            Name of the vertex.
        source : bool, optional
            Is the source vertex (default is False).
        sink : bool, optional
            Is the sink vertex (default is False).
        '''

        self.name = name
        self.source = source
        self.sink = sink

class Network:
    '''
    A class used to represent the network.
    '''

    def __init__(self):

        self.network = {}
        self.vertices = []

    def add_vertices(self, vertices: list) -> None:
        '''
        Add vertices to the network.

        Parameters
        ----------
        vertices : list
            List of Vertex objects.
        '''
        for v in vertices:
            self.vertices.append(v)
            self.network[v.name] = []

    def add_edges(self, edges: list)-> None:
        '''
        Add edges to the network.

        Parameters
        ----------
        edges : list
            List of Edge objects.
        '''

        for edge in edges:

            self.network[edge.start].append(edge)

    def get_path(self, start:str, end:str, path:list) -> list:
        '''
        Calculates the residual capacity on the given path.

        Parameters
        ----------
        start : str 
            Start node of the edge.
        end : str
            End node of the edge.
        path : list
            Capacity of the node (default is 0).

        Returns
        -------
        list
            A list representing the path.
        '''

        # We've walked through the network's path.
        if start is end:
            return path

        for edge in self.network[start]:
            
            residual_capacity = edge.capacity - edge.flow

            #  If capacity is greater, than 0 and edge is not in the path.
            if residual_capacity > 0 and not (edge, residual_capacity) in path:

                # Calculate the path for the next edge.
                result = self.get_path(edge.end, end, path + [(edge, residual_capacity)])

                if result != None:
                    return result


class CalculateFlow(Network):

    '''
    A class used to calculate  the max flow/ capacity of the network.
    '''

    def __init__(self):

        super().__init__()
        
    def calculate_max_flow(self) -> int:
        '''
        Calculates the max flow of the network.

        Returns
        -------
        int
            The maximum capacity/ flow of the given network.
        '''

        # Get source and sink of the network.
        source = self.vertices[0]
        sink = self.vertices[1]

        path = self.get_path(source.name, sink.name, [])

        while path != None:

            # Get smallest capacity on the given path.
            flow = min(edge[1] for edge in path)

            for edge, _ in path:
                edge.flow += flow
            
            path = self.get_path(source.name, sink.name, [])

        # Sum up the flows on the paths.
        return sum(edge.flow for edge in self.network[source.name])


if __name__ == '__main__':
    '''
        Implementation of the Ford-Fulkerson max flow algorithm.
    '''

    calc_flow = CalculateFlow()

    # Adding vertexes to the network.
    v = [
        Vertex(name='s', source=True),
        Vertex(name='t', sink=True),
        Vertex(name='a'),
        Vertex(name='b'),
        Vertex(name='c'),
        Vertex(name='d')
    ]
    calc_flow.add_vertices(vertices=v)


    # Adding edges to the network.
    e = [
        Edge(start='s', end='a', capacity=4),
        Edge(start='a', end='b', capacity=4),
        Edge(start='b', end='t', capacity=2),
        Edge(start='s', end='c', capacity=3),
        Edge(start='c', end='d', capacity=6),
        Edge(start='d', end='t', capacity=6),
        Edge(start='b', end='c', capacity=3)
    ]
    calc_flow.add_edges(edges=e)

    result = calc_flow.calculate_max_flow()
    print(result) # Should be 7.
