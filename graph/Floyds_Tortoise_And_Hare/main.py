class Node:

    ''' Class to represent a node in the graph. '''

    def __init__(self, value: int, next_node: 'Node' = None):

        self.value = value
        self.next = next_node

    def __repr__(self):

        return "Node <{}>".format(self.value)


def find_cycle(start_node: Node) -> bool:
    ''' 
    Floyd's Cycle-Finding Algorithm.
    
    Parameters
    ----------
    start_node : Node
        First node in the graph.

    Returns
    -------
    bool
        True -> cycle found, False -> no cycle.
    '''

    tortoise, hare = start_node, start_node

    while hare is not None and hare.next is not None:

        # Tortoise (slow) moves by 1, while hare (fast) moves by 2.
        tortoise, hare = tortoise.next, hare.next.next

        # Cycle  found.
        if tortoise == hare:
            return True

    # No cycle.
    return False


if __name__ == '__main__':

    # Winthout cycle -> False.
    linked_list = Node(1, Node(2, Node(3, Node(4))))
    res = find_cycle(linked_list)

    print(res)

    # With cycle.
    node4 = Node(4)
    linked_list = Node(1, Node(2, Node(3, node4)))
    node4.next = linked_list
    res = find_cycle(linked_list)

    print(res)