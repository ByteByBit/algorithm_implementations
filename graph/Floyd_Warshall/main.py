def floyd_warshall(graph: list):

    d = list(map(lambda i: list(map(lambda j: j, i)), graph))
    num_vertices = len(graph)

    for k in range(num_vertices):

        for i in range(num_vertices):

            for j in range(num_vertices):

                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


if __name__ == '__main__':


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