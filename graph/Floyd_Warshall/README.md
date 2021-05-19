# Floyd-Warshall Algorithm

<p>The Floyd-Warshall Algorithm is used for solving All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. </p>
<p>Time complexity:</p>
<ul>
    <li>O(V<sup>3</sup>)</li>
</ul>
<p>Space complexity:</p>
<ul>
    <li>O(V<sup>2</sup>)</li>
</ul>
<p>Where V represents the vertices.</p>
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