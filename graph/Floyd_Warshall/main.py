

def floyd_warshall(graph: list):

    d = list(map(lambda i: list(map(lambda j: j, i)), graph))
    num_vertices = len(graph)

    for i in range(num_vertices):

        for j in range(num_vertices):

            for k in range(num_vertices):

                d[j][k] = min(d[j][k],
                d[j][i] + d[i][k])

    
    return d


if __name__ == '__main__':
    '''
    Visual representation of the given graph.

             22
       (0)------->(5)
        |         /|\
        |          |
      5 |          | 7
        |          | 
       \|/         |
       (1)        (4)         
        |         /|\
        |          |
      3 |          | 1
        |          | 
       \|/         |
       (2)------->(3)
             4       
             
    Expected result:
    Shortest distance matrix
    (0) -> [0, 5, 8, 12, 13, 20]
    (1) -> [INF, 0, 3, 7, 8, 15]
    (2) -> [INF, INF, 0, 4, 5, 12]
    (3) -> [INF, INF, INF, 0, 1, 8]
    (4) -> [INF, INF, INF, INF, 0, 7]
    (5) -> [INF, INF, INF, INF, INF, 0]
    '''
    INF = 9999
    graph = [
        [0, 5, INF, INF, INF, 22],
        [INF, 0, 3, INF, INF, INF],
        [INF, INF, 0, 4, INF, INF],
        [INF, INF, INF, 0, 1, INF],
        [INF, INF, INF, INF, 0, 7],
        [INF, INF, INF, INF, INF, 0]
    ]
    res = floyd_warshall(graph)

    print(res)