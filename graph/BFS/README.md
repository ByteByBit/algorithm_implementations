# Bredth First Search Algorithm

<h2>Time complexity: O(V+E), where V is the number of vertices and E is the number of edges in the graph.</h2>
<h2>Space complexity: O(V), where V is the number of vertices in the graph.</h2>
<h2>Implementation:</h2>
<ul>
    <li>Store the graph in a dictionary</li>
    <li>Create two objects, one:</li>
        <ol>
            <li>visited (list): store here the already visited vertices/ nodes</li>
            <li>queue (dequeue): to store the upcoming vertices.</li>
        </ol>
    <li>Dequeue the root/ start node from the queue and mark it visited</li>
    <li>Iterate over it's adjacent nodes, if any of them is not visited, we have our next participant</li>
    <li>Mark it visited</li>
    <li>Start over with the stranger node</li>
    <li>Continue until we are out of nodes</li>
</ul>
<h3>The difference between Breadth First Search and Depth First Search is: BFS first goes horizontal, then vertical, while DFS the opposite way.</h3>
    